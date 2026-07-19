# H₂(q) instances + algebra-hom inclusion — the concrete tower bottom complete (2026-07-19)

**Bean:** `qou-h2in`. **Lean:** [`QOU/Machinery/HeckeH2AlgebraInstance.lean`](../../content/quantum-observable-universe/lean/QOU/Machinery/HeckeH2AlgebraInstance.lean)
— sorry-free, `lean`-direct exit 0. §7c-generic (`[CommRing R]`).

## What landed

- **`H2A R h`** — the rank-two Hecke algebra `H₂(q) = span{γ, σ₀}` (rank-one
  Hecke-quadratic product) as a genuine **`CommRing`** + **`Algebra R`**.
- **`markovTrace_H2A`** — the n=2 `MarkovTrace` instance (`trace₂ = a + z·b`).
  With `markovTrace_H3A`, **both concrete rungs now inhabit the class**.
- **`iotaAlg : H2A R h →ₐ[R] H3A R h`** — the tower inclusion as an honest
  R-algebra homomorphism (multiplicativity = the merged `iota23_mul`).
- **`trace3_iotaAlg_stabilizes`** — `trace₃(ι x) = trace₂ x` along the
  AlgHom: the bottom stabilization step **in exactly the shape the
  `MarkovStabilization` class asks of its `ι : Hn →ₐ Hn1` parameter**.

## Tower state (concrete layer COMPLETE through n=4)

```
n=2: CommRing + Algebra + MarkovTrace instance          THIS
2→3: AlgHom inclusion + stabilization at instance shape THIS
n=3: algebra object + Ring/Algebra + MarkovTrace        merged (#4050, #4051)
n=4: σ-tables + all presentation-law kinds              merged (#4052)
3→4: stabilization + M3 reduction                       merged (#4052)
n→∞: general-n classes (H_∞ binders)                    OPEN — the next wall
```

Honesty: general-n class instances stay OPEN; nothing wired; `1/(8π)`
stays phase-4.
