import type { Product, Recommendation } from '../types'

interface RecommendationPanelProps {
  recommendation: Recommendation
  product?: Product
}

export function RecommendationPanel({ recommendation, product }: RecommendationPanelProps) {
  return (
    <section className="panel recommendation-panel">
      <h2>Recommended for you</h2>
      <div className="recommendation-card">
        {product && (
          <img src={product.image_url} alt={product.title} className="rec-image" />
        )}
        <div>
          <h3>{recommendation.title}</h3>
          {recommendation.score != null && (
            <p className="rec-score">Match score: {recommendation.score}</p>
          )}
          <ul>
            {recommendation.reasons.map((reason) => (
              <li key={reason}>{reason}</li>
            ))}
          </ul>
        </div>
      </div>
    </section>
  )
}
