# H₄(q) Wedderburn decomposition — symbolic data (bean qou-yidw)

Conventions (verified against the Lean sources, see "convention surprises"
below): Hecke quadratic $x^2 = h\,x + 1$, $h = q - q^{-1}$, eigenvalues
$\ell_+ = q$, $\ell_- = -q^{-1}$.

## Basis (from `HeckeH4StabilizationRung.lean` / preflight witness)

24 canonical S₄ words, H₃ Lean basis `[γ, σ₀, σ₁, σ₁σ₀, σ₀σ₁, σ₀σ₁σ₀]`
as prefix, then the remaining 18 sorted by (length, canonical word):

```
[[], [0], [1], [1, 0], [0, 1], [0, 1, 0], [2], [1, 2], [2, 0], [2, 1], [0, 1, 2], [1, 2, 0], [1, 2, 1], [2, 0, 1], [2, 1, 0], [0, 1, 2, 0], [0, 1, 2, 1], [1, 2, 0, 1], [1, 2, 1, 0], [2, 0, 1, 0], [0, 1, 2, 0, 1], [0, 1, 2, 1, 0], [1, 2, 0, 1, 0], [0, 1, 2, 0, 1, 0]]
```

Word $(i_0, i_1, \dots)$ is the product $\sigma_{i_0}\sigma_{i_1}\cdots$;
right multiplication $u\cdot b_j$ composes `mulσ` along the word applying
$\sigma_{i_0}$ FIRST (right actions anti-compose); the representation of a
word is the plain product $S_{i_0} S_{i_1} \cdots$ (H3 `blockOf` pattern).

## The two characters

* $\chi_+$ (partition $(4)$): $\sigma_i \mapsto q$; basis word of length
  $\ell$ contributes $q^\ell$.
* $\chi_-$ (partition $(1^4)$): $\sigma_i \mapsto -q^{-1}$; contributes
  $(-q^{-1})^\ell$.

## Seminormal blocks (b-entry of each mixing block normalized to 1)

Tableaux orders: $(2,2)$: `[12|34], [13|24]`; $(3,1)$: `[123|4], [124|3],
[134|2]`; $(2,1,1)$: `[12|3|4], [13|2|4], [14|2|3]`.

### Partition (2,2) — 2-dimensional

$$ S_0 = \begin{pmatrix} q & 0 \\ 0 & - \frac{1}{q} \end{pmatrix} $$

$$ S_1 = \begin{pmatrix} - \frac{1}{q^{3} + q} & 1 \\ \frac{q^{4} + q^{2} + 1}{q^{4} + 2 q^{2} + 1} & \frac{q^{3}}{q^{2} + 1} \end{pmatrix} $$

$$ S_2 = \begin{pmatrix} q & 0 \\ 0 & - \frac{1}{q} \end{pmatrix} $$

(The $S_1$ mixing block is *identical* to `HeckeH3BlockRep.S1` — same axial
distance $-2$.)

### Partition (3,1) — 3-dimensional

$$ S_0 = \begin{pmatrix} q & 0 & 0 \\ 0 & q & 0 \\ 0 & 0 & - \frac{1}{q} \end{pmatrix} $$

$$ S_1 = \begin{pmatrix} q & 0 & 0 \\ 0 & - \frac{1}{q^{3} + q} & 1 \\ 0 & \frac{q^{4} + q^{2} + 1}{q^{4} + 2 q^{2} + 1} & \frac{q^{3}}{q^{2} + 1} \end{pmatrix} $$

$$ S_2 = \begin{pmatrix} - \frac{1}{q^{5} + q^{3} + q} & 1 & 0 \\ \frac{q^{8} + 2 q^{6} + 2 q^{4} + 2 q^{2} + 1}{q^{8} + 2 q^{6} + 3 q^{4} + 2 q^{2} + 1} & \frac{q^{5}}{q^{4} + q^{2} + 1} & 0 \\ 0 & 0 & q \end{pmatrix} $$

### Partition (2,1,1) — 3-dimensional

$$ S_0 = \begin{pmatrix} q & 0 & 0 \\ 0 & - \frac{1}{q} & 0 \\ 0 & 0 & - \frac{1}{q} \end{pmatrix} $$

$$ S_1 = \begin{pmatrix} - \frac{1}{q^{3} + q} & 1 & 0 \\ \frac{q^{4} + q^{2} + 1}{q^{4} + 2 q^{2} + 1} & \frac{q^{3}}{q^{2} + 1} & 0 \\ 0 & 0 & - \frac{1}{q} \end{pmatrix} $$

$$ S_2 = \begin{pmatrix} - \frac{1}{q} & 0 & 0 \\ 0 & - \frac{1}{q^{5} + q^{3} + q} & 1 \\ 0 & \frac{q^{8} + 2 q^{6} + 2 q^{4} + 2 q^{2} + 1}{q^{8} + 2 q^{6} + 3 q^{4} + 2 q^{2} + 1} & \frac{q^{5}}{q^{4} + q^{2} + 1} \end{pmatrix} $$

All three blocks verified symbolically: Hecke quadratic for each $S_i$, both
adjacent braid relations, far commutation $S_0 S_2 = S_2 S_0$.

Structure notes: every 2×2 mixing block has the H3BlockRep shape
$[[a, 1], [a(h-a)+1, h-a]]$ with $a = h/(1-q^{-2d})$ for axial distance
$d$.  The $d=-2$ block (all three partitions' $\sigma_1$-edge) is exactly
`HeckeH3BlockRep.S1`; the $d=-3$ block (the $\sigma_2$-edge of $(3,1)$ and
$(2,1,1)$) has $a = -1/(q(q^4+q^2+1))$, $h-a = q^5/(q^4+q^2+1)$ and
$c$-entry $(q^2+1)^2(q^4+1)/(q^4+q^2+1)^2$ — the $[4]$-type factor
$q^4+1$ enters here, matching its appearance in $\det A$.

## Convention surprises found in the Lean file

None that contradict the task assumptions, but three facts worth pinning:

1. The 24-word basis order is NOT plain length-lex over all of S₄: the six
   H₃ words come FIRST (in the H₃ Lean order, so word 3 is $\sigma_1
   \sigma_0$ and word 4 is $\sigma_0\sigma_1$), and only the remaining 18
   words are sorted by (length, canonical word).  Canonical words come from
   the leftmost-descent factorization (see `canonical_word` above).
2. `mulσᵢ` is RIGHT multiplication; each output entry $k$ is
   $v_a + h\,v_k$ (the $h$-coefficient always sits on the output index
   itself) — verified entry-for-entry against the exact Iwahori–Hecke
   length rule.
3. $\rho(\text{word})$ must be the product of the $S$ matrices in word
   order (NOT reversed): right actions anti-compose, which is already
   accounted for in the `mulNF` pattern `u·b_j = mulσ_{i_0}` first.

## Determinant of the 24×24 coordinate matrix

$$ \det A = - \frac{\left(q^{2} + 1\right)^{24} \left(q^{4} + 1\right)^{10} \left(q^{2} - q + 1\right)^{3} \left(q^{2} + q + 1\right)^{3}}{q^{50}} $$

## Genericity hypotheses (the ≠ 0 conditions read off det A)

* $q \neq 0$
* $q^{2} + 1 \neq 0$
* $q^{4} + 1 \neq 0$
* $q^{2} + q + 1 \neq 0$
* $q^{2} - q + 1 \neq 0$

## Verification summary

* [PASS] basis_words_match_preflight_witness — 24 canonical words, H3 Lean prefix
* [PASS] lean_operator_tables_match_length_rule — mulσ₀/mulσ₁/mulσ₂ entries of HeckeH4StabilizationRung.lean == exact Iwahori–Hecke length-rule matrices, entry-for-entry
* [PASS] block_(2,2)_relations — Hecke quadratic ×3, braid σ₀σ₁σ₀=σ₁σ₀σ₁, braid σ₁σ₂σ₁=σ₂σ₁σ₂, far commutation σ₀σ₂=σ₂σ₀ — exact over ℚ(q)
* [PASS] block_(3,1)_relations — Hecke quadratic ×3, braid σ₀σ₁σ₀=σ₁σ₀σ₁, braid σ₁σ₂σ₁=σ₂σ₁σ₂, far commutation σ₀σ₂=σ₂σ₀ — exact over ℚ(q)
* [PASS] block_(2,1,1)_relations — Hecke quadratic ×3, braid σ₀σ₁σ₀=σ₁σ₀σ₁, braid σ₁σ₂σ₁=σ₂σ₁σ₂, far commutation σ₀σ₂=σ₂σ₀ — exact over ℚ(q)
* [PASS] block_2_2_S1_equals_H3_S1 — (2,2) σ₁ mixing block == HeckeH3BlockRep.S1 (same axial distance −2)
* [PASS] det_nonzero — -(q**2 + 1)**24*(q**4 + 1)**10*(q**2 - q + 1)**3*(q**2 + q + 1)**3/q**50
* [PASS] A_times_Ainv_is_identity — A·A⁻¹ = A⁻¹·A = 1, exact over the fraction field of QQ[q]
* [PASS] coordinate_map_is_algebra_map_5_random_pairs — coords(u·v) == blockwise product at q ∈ ['7/5', '3/2', '5/3', '9/7', '11/4'], random integer u,v; unit ↦ (1,1,I₂,I₃,I₃)
* [PASS] numeric_roundtrip_Ainv_A — q = 7/5

Full matrices `A`, `A⁻¹` (entries cancelled over ℚ(q)) in `data.json`.
Reproduce with `python3 derive.py`.
