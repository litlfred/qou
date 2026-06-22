# Habiro-WRT(S³/2I) push: the Lawrence–Zagier false theta computed, the frontier made concrete

**Date:** 2026-06-22
**Branch:** `claude/keystone-habiro-wrt-s3-2i-2026-06-22`
**Status:** Positive — the WRT q-series is now operational in the corpus and the residual frontier is
made concrete (and type-corrected). No fit; the bare-invariant ↔ W_λ equality is NOT claimed.
**Bean:** [`s5bb`](../../.beans/s5bb--s5-so3-keystone.md)
**Follows:** [`2026-06-22-keystone-modular-category-identification.md`](2026-06-22-keystone-modular-category-identification.md)
**Script:** [`scripts/keystone_habiro_wrt_s3_2i_probe.py`](scripts/keystone_habiro_wrt_s3_2i_probe.py)
**Witness:** [`computations/keystone-habiro-wrt-s3-2i.witness.json`](../../computations/keystone-habiro-wrt-s3-2i.witness.json)

## The formula (pinned from the literature, not guessed)

The WRT invariant of the Poincaré sphere `S³/2I = Σ(2,3,5)` is governed by the Lawrence–Zagier
false (partial) theta function (Lawrence–Zagier 1999; Hikami, *Quantum Invariant, Modular Form, and
Lattice Points*; arXiv:1811.05376, arXiv:2205.01282):

$$\Psi(q)=\sum_{a\in\{1,11,19,29\}}\widetilde\Psi_{30}^{(a)}(q)=\sum_{n\ge0}\chi(n)\,q^{n^2/120},$$

with `χ` the odd periodic function mod 60:

| `n mod 60` | 1, 11, 19, 29 | 31, 41, 49, 59 | else |
|------------|---------------|----------------|------|
| `χ(n)` | +1 | −1 | 0 |

`P = 30 = h(E₈)` (Coxeter number), `4P = 120`. The support residues `{1,11,19,29}` are the
icosahedral/E₈ data of `Σ(2,3,5)`. (An overall `q^{±1/120}` prefactor — i.e. `n²/120` vs
`(n²−1)/120` — is convention-dependent; it shifts the value by ~0.09 % at the substrate and does not
affect any structural conclusion or ratio below.)

## The regime fact (the substrate is on the *other* side of the unit circle)

`Ψ(q)` converges only for `|q| < 1` (roots of unity sit on the boundary — that is where the WRT
invariant is recovered as a radial limit). The substrate `q₀ = 1.10998` is **> 1, outside the disk**.
Its **bar image `1/q₀ ≈ 0.90092` is inside**. So the type-correct evaluation goes through the
`q ↦ q⁻¹` bar involution — the *same* involution the entire `c_k` / Reeb-phase / bar-parity corpus
runs on. Computed (50 dps, converged; tail `= 0` by 1200 terms — the false theta converges fast):

| quantity | value |
|----------|-------|
| `Ψ(1/q₀)` | **2.32957704683293** |
| `Θ_{3/2}(1/q₀)` (weight-3/2 partner `Σ n·χ(n) q^{n²/120}`) | 10.4959110098 |

(For reference: `Ψ(0.5)=1.6195`, `Ψ(0.9)=2.3317`, `Ψ(0.99)=2.0209`.)

## Type-correct assessment (no forcing)

- `Ψ(1/q₀) ≈ 2.3296` is **one** closed-manifold invariant; `W_λ` is a **λ-family**
  (electron `d_q(3,1,1)=6.2204`, muon `d_q(3,2)=5.2204`, `[5]_q!=131.31`, `D²=Σd_q²=128.98`). A direct
  `Ψ = W_λ` numerical equality is a **type mismatch** and is **not** asserted (and no clean small-integer
  / q-integer match to `Ψ(1/q₀)` was sought — that would be the numerology trap the discipline forbids).
- **The link is structural.** The support residues `{1,11,19,29 mod 60}` *are* the icosahedral/E₈ data
  (`P=30=h(E₈)`) — the **same** icosahedral input the `A₅ ⊂ SO(3)` fibre map and the `W_λ` blocks carry.
  The bare `Σ(2,3,5)` invariant **selects** that modular data; it does not, by itself, resolve the
  λ-family.

## What the push establishes (and the sharpened frontier)

**Established this session:**
1. The Lawrence–Zagier WRT q-series for `Σ(2,3,5)` is now **operational in the corpus** (script +
   witness), with the character pinned to the literature and the E₈/icosahedral support verified.
2. The **regime bridge** is identified: WRT series live at `|q|<1`; the substrate `q₀>1`; they are
   joined by the `q↦q⁻¹` bar involution (`q₀ ↔ 1/q₀`). The Habiro ring is the object that makes both
   the root-of-unity and the generic-`q` evaluations one element — so the generic-`q₀` side is the
   bar image of the convergent WRT series.

**The sharpened (type-correct) frontier — what a closure now requires:**
the bare closed-manifold invariant `Ψ(Σ(2,3,5))` is a single number, so reproducing the `W_λ`
**family** needs the **WRT TQFT with λ-coloured insertions** (the coloured Σ(2,3,5) invariants / the
modular `S`-matrix data that the surgery presentation supplies), evaluated through the bar/Habiro
bridge — **not** the closed-manifold number computed here. That is the concrete, finitely-stated next
object; it is representation-theoretic + q-series, not differential geometry.

No fit; nothing wired; `c_k`/`Δ_λ` cal-anchored.

## Cross-references

- [`2026-06-22-keystone-modular-category-identification.md`](2026-06-22-keystone-modular-category-identification.md) — the non-compact `E_q(2)` identification this builds on.
- [`2026-06-13-reeb-phase-qbessel-identification.md`](2026-06-13-reeb-phase-qbessel-identification.md) — the q-Bessel / bar structure the regime bridge uses.
- [`2026-06-16-s5so3-markov-weighting-sasakian-scope.md`](2026-06-16-s5so3-markov-weighting-sasakian-scope.md) — the `W_λ` target + the WRT/Habiro redirect.
- Sources: Lawrence–Zagier, *Modular forms and quantum invariants of 3-manifolds* (1999); Hikami, arXiv:math-ph/0504082, arXiv:1811.05376; Andersen–Mistegård, arXiv:2205.01282.
