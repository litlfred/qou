# qNumberSym_classical_limit

The theorem `qNumberSym_classical_limit` in `q-casimir-classical-limit.lean` requires evaluating the limit of `qIntBalZ` as `q \to 1`. Since `qIntBalZ q n` is `(q^n - q^{-n})/(q - q^{-1})`, this is a L'Hopital rule application or a geometric series expansion.
This proof requires limits over polynomials or geometric series which are currently not straightforward without additional Mathlib infrastructure.
