import type { Product } from '../types'

interface ProductGridProps {
  products: Product[]
  recommendedId?: string
}

export function ProductGrid({ products, recommendedId }: ProductGridProps) {
  if (products.length === 0) {
    return <p className="empty-state">No products matched your requirements.</p>
  }

  return (
    <div className="product-grid">
      {products.map((product) => (
        <article
          key={product.id}
          className={`product-card${product.id === recommendedId ? ' highlighted' : ''}`}
        >
          <img src={product.image_url} alt={product.title} loading="lazy" />
          <div className="product-body">
            <h3>{product.title}</h3>
            <p className="product-meta">
              <span className="price">₹{product.price_inr.toLocaleString('en-IN')}</span>
              <span className="rating">★ {product.rating.toFixed(1)}</span>
            </p>
            <p className="product-desc">{product.description}</p>
            <button type="button" className="cart-btn">
              Add to Cart
            </button>
          </div>
        </article>
      ))}
    </div>
  )
}
