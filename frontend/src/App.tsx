import { useState } from 'react'
import { shopSearch } from './api/client'
import { AgentTracePanel } from './components/AgentTracePanel'
import { ComparisonPanel } from './components/ComparisonPanel'
import { ProductGrid } from './components/ProductGrid'
import { RecommendationPanel } from './components/RecommendationPanel'
import { SearchBar } from './components/SearchBar'
import type { ShopResponse } from './types'
import './App.css'

const DEFAULT_QUERY =
  'Find wireless headphones under ₹3500 with good sound quality'

function App() {
  const [query, setQuery] = useState(DEFAULT_QUERY)
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState<string | null>(null)
  const [result, setResult] = useState<ShopResponse | null>(null)

  async function handleSearch() {
    setLoading(true)
    setError(null)
    try {
      const data = await shopSearch(query.trim())
      setResult(data)
    } catch (err) {
      setError(err instanceof Error ? err.message : 'Search failed')
      setResult(null)
    } finally {
      setLoading(false)
    }
  }

  const recommendedProduct = result?.products.find(
    (p) => p.id === result.recommendation.product_id,
  )

  return (
    <div className="app">
      <header className="header">
        <div>
          <p className="brand-kicker">Multi-Agent AI Shopping</p>
          <h1>ShopEasy</h1>
          <p className="subtitle">
            Describe what you need — requirement, search, comparison, and recommendation agents
            work together.
          </p>
        </div>
      </header>

      <SearchBar
        value={query}
        onChange={setQuery}
        onSubmit={handleSearch}
        loading={loading}
      />

      {error && <p className="error-banner">{error}</p>}

      {loading && (
        <div className="loading-skeleton" aria-live="polite">
          <div className="sk-line wide" />
          <div className="sk-line" />
          <div className="sk-grid">
            <div className="sk-card" />
            <div className="sk-card" />
            <div className="sk-card" />
          </div>
        </div>
      )}

      {result && !loading && (
        <>
          <div className="requirements-chip">
            <span>{result.requirements.category}</span>
            <span>Budget ≤ ₹{result.requirements.max_price_inr.toLocaleString('en-IN')}</span>
            {result.requirements.priorities.length > 0 && (
              <span>Priorities: {result.requirements.priorities.join(', ')}</span>
            )}
          </div>

          <div className="layout">
            <main>
              <h2 className="section-title">Matching products</h2>
              <ProductGrid
                products={result.products}
                recommendedId={result.recommendation.product_id}
              />
            </main>
            <aside className="sidebar">
              <RecommendationPanel
                recommendation={result.recommendation}
                product={recommendedProduct}
              />
              <ComparisonPanel comparison={result.comparison} />
              <AgentTracePanel trace={result.trace} />
            </aside>
          </div>
        </>
      )}
    </div>
  )
}

export default App
