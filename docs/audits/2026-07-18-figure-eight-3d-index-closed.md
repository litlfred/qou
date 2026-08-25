# The GGM 3D-index of 4₁ — gluing closed and validated (2026-07-18)

**Tier:** closes the G3 3d-index gluing opened in
[`2026-07-18-tetrahedron-index-triality-pin.md`](2026-07-18-tetrahedron-index-triality-pin.md)
(#3868) and the attack audit
[`2026-07-14-g3-stokes-via-3d-index.md`](2026-07-14-g3-stokes-via-3d-index.md) (#3805).
Audit-only; no production wiring; scope-(a); comparison-only.

## Result

The figure-eight 3D-index is assembled on the triality-validated tetrahedron index
`I_Δ` and **matches the primary source exactly** (probe
[`figure_eight_3d_index.py`](../../computations/probes/figure_eight_3d_index.py) +
witness, exact integer q-series, 3 peripheral classes to q¹⁰):

$$I_{4_1}(0) = 1 - 2q - 3q^2 + 2q^3 + 8q^4 + 18q^5 + 18q^6 + 14q^7 - 12q^8 - 52q^9 - 106q^{10} + \cdots$$

`I_T(λ)` and `I_T(2µ)` also match. No negative q-powers (a genuine power series, as
required for the 1-efficient triangulation, Cor 10.21). Source: Garoufalidis–Hodgson–
Hoffman–Rubinstein, *The 3D-index and normal surfaces* (arXiv:1604.02688), Example 4.1,
supplied by the owner (`library/arxiv-1604.02688v1/1604.02688v1.pdf`, commit `39e0b64b`).

The gluing formula is the paper's Example 4.1:
$$I_T(x\mu + y\lambda) = \sum_{k\in\mathbb Z} q^k\, J_\Delta(2k,k,x)\, J_\Delta(2k-x+2y,\,k,\,-2y),$$
with `J_Δ` the **symmetric** tetrahedron index (eq 4),
`J_Δ(a,b,c) = (−q^{1/2})^{−b} I_Δ(b−c, a−b)`, and `J_Δ(A,B,0) = I_Δ(−A,B)` (eq 6).

## The "normalization" was the triality all along

The three equal forms of eq (4) are **exactly the S₃ triality of `I_Δ` pinned
empirically in #3868**: the cyclic generator
`I_Δ(m,e) = (−q^{1/2})^m · I_Δ(−e−m, m)` is the equality of eq (4)'s three
expressions. So the "missing per-term normalization prefactor" the gluing needed is
**not** a new open object — it is the `(−q^{1/2})^{−b}` weight that turns `I_Δ` into the
S₃-invariant `J_Δ`, and that turns each summand into a genuine power series of q-degree
~`2k²` (so only `|k| ≲ √(N/2)` contribute to `qᴺ` — a finite sum per order).

## Correction to the #3868 record (STRICT — read this)

The follow-on section of the #3868 audit reported the gluing as **blocked on a
primary-source normalization**, against a target `[1, −8, −9, 18, 46, 90]`. Both were
wrong and are corrected here:

1. **The target `[1,−8,−9,18,46,90]` was a bad secondary value** (a garbled web-search
   figure, never in the primary source). The **correct** figure-eight index is
   `[1, −2, −3, 2, 8, 18, 18, 14, −12, −52, −106]` (1604.02688 Ex 4.1), reproduced
   here exactly.
2. **The gluing was not blocked.** The "normalization gap" was the `(−q^{1/2})^{−b}`
   symmetrization of eq (4) — i.e. the triality already pinned in #3868. With `J_Δ`
   in place the naive-sum divergence disappears (each term is a power series) and the
   index closes.

The #3868 triality pin itself stands unchanged and correct; only its *follow-on
speculation* about a blocking normalization is superseded by this validated assembly.

## Next (the G3 Stokes datum)

With the 3D-index in hand as an exact q-series, the GGM resurgent Stokes data is read
from its asymptotics / the Borel structure of the state-integral it packages — the
odd-face action cross-checked against the `[0.147, 0.168]` band (merged #3810 lever-1)
and the even-face `Vol(4₁)/π`. That extraction is the remaining G3 step (#3805); it is
now standing on a *validated* index rather than a candidate one. No `A_ω` or `c_k`
wired; nothing reaches production until a Stokes constant is genuinely derived. scope-(a).
