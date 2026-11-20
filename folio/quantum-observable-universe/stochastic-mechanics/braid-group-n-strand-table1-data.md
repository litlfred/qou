| Lean object | Role |
|---|---|
| `TypedCrossing n` | A single typed crossing: generator index $i \in \mathrm{Fin}(n-1)$ + sign $\pm 1$ |
| `BraidWord n` | List of typed crossings (the empty word is the identity braid) |
| `BraidWord.writhe` | Net signed crossing count (algebraic) |
| `closureN` | Markov closure to a `Link`, **opaque at general $n$**, concrete at $n=2$ via `closure2` |
| `HeckeQuotient n q` | Class encoding the Hecke quadratic relation $\sigma_i^2 = (q - q^{-1})\sigma_i + 1$ |
| `MarkovTraceN n q` | Generalised Markov-trace axioms M1-M4 (Jones 1985); the genuine trace structure is `OcneanuTrace.MarkovTrace` |
