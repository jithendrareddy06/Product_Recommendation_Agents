interface SearchBarProps {
  value: string
  onChange: (value: string) => void
  onSubmit: () => void
  loading: boolean
}

export function SearchBar({ value, onChange, onSubmit, loading }: SearchBarProps) {
  return (
    <form
      className="search-bar"
      onSubmit={(e) => {
        e.preventDefault()
        onSubmit()
      }}
    >
      <input
        type="text"
        placeholder='Try: "Find wireless headphones under ₹3500 with good sound quality"'
        value={value}
        onChange={(e) => onChange(e.target.value)}
        disabled={loading}
        aria-label="Natural language product search"
      />
      <button type="submit" disabled={loading || !value.trim()}>
        {loading ? 'Agents working…' : 'Search with AI'}
      </button>
    </form>
  )
}
