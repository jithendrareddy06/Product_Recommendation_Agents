import type { ComparisonMatrix } from '../types'

interface ComparisonPanelProps {
  comparison: ComparisonMatrix
}

export function ComparisonPanel({ comparison }: ComparisonPanelProps) {
  const { product_ids, product_titles, rows } = comparison
  if (product_ids.length === 0) {
    return null
  }

  return (
    <section className="panel comparison-panel">
      <h2>AI Agent Comparison</h2>
      <div className="table-wrap">
        <table>
          <thead>
            <tr>
              <th>Criteria</th>
              {product_ids.map((id) => (
                <th key={id}>{product_titles[id] ?? id}</th>
              ))}
            </tr>
          </thead>
          <tbody>
            {rows.map((row) => (
              <tr key={row.criterion}>
                <td>{row.criterion}</td>
                {product_ids.map((id) => (
                  <td key={id}>{row.values[id] ?? 'N/A'}</td>
                ))}
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </section>
  )
}
