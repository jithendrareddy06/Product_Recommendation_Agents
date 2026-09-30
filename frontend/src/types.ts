export interface StructuredRequirements {
  category: string
  max_price_inr: number
  keywords: string[]
  priorities: string[]
}

export interface Product {
  id: string
  title: string
  category: string
  price_inr: number
  rating: number
  image_url: string
  description: string
  specs: Record<string, string>
}

export interface ComparisonRow {
  criterion: string
  values: Record<string, string>
}

export interface ComparisonMatrix {
  product_ids: string[]
  product_titles: Record<string, string>
  rows: ComparisonRow[]
}

export interface Recommendation {
  product_id: string
  title: string
  score: number | null
  reasons: string[]
}

export interface AgentTraceStep {
  agent: string
  summary: string
  detail: Record<string, unknown>
}

export interface ShopResponse {
  query: string
  requirements: StructuredRequirements
  products: Product[]
  comparison: ComparisonMatrix
  recommendation: Recommendation
  trace: AgentTraceStep[]
}
