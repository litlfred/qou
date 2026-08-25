# Door-iv: tensor-square MATRIX realization of GGM from C1 — cross term is slope-0 but does not intertwine (2026-07-20)

**Bean:** `qou-vim1` · **Branch:** `claude/qlift-borel-kernel-derivation-2026-07-20`
**Status:** AUDIT — probe complete. **Precondition MET** (owner's structural
insight confirmed); **matrix realization scope-(a) REFUTED**. No open item
declared; no conjecture status changed.

## 0. What this attacks (and why it is NOT Door-iii)

Door-iii / Door-iii-followup ([`…doorIII-followup`](2026-07-20-qlift-doorIII-followup.md))
REFUTED a **scalar, m-independent** linear combo of C1's symmetric squares.
Root cause: both C1 branches came from **forward** recursion, both decay
`q^{−m²/4}` (isoclinic), so `f₊f₋` sat at **slope −1**, not the slope-0 datum
the anisoclinic {−1,+1} GGM needs.

- **C1** (proved q-lift): `[m+2]_q b_{m+2}=b_{m+1}+b_m`, ∞-slopes **{½,½}**
- **GGM** (eq 49, `library/arxiv-2012.00062v3/2012.00062v3.pdf` p.14): `y_{m+1}=(2−q^m)y_m−y_{m−1}`, **{−1,+1}**

**Owner insight (the key):** GGM should be realized WITHIN a matrix / the
tensor square `C1⊗C1`, with the slope-0 cross term `f₊f₋` as the off-diagonal
**anisoclinic coupler** a scalar combination structurally cannot supply. **Fix
vs Door-iii:** genuinely separate a *growing* branch from a *decaying* branch.
C1 is isoclinic — it has no native growing branch — so the growing companion is
the **q-factorial carrier lift** (the very carrier the q-lift was proved on,
`qlift_normalized_kernel_exists`): `g_m := [m]_q!·b_m ~ q^{+m²/4}` (satisfying
`g_{m+2}=g_{m+1}+[m+1]_q g_m`). Set `f₊:=g` (growing), `f₋:=b` (forward C1,
decaying), so `f₊f₋ = [m]_q!·b² ~ q^0` is **genuinely slope-0**. The tensor
square then carries slopes **{+1,0,−1} ⊇ GGM {+1,−1}** — anisoclinic, so
Door-i's isoclinicity (b)-exclusion of *C1 itself* does **not** forbid this route.

## 1. The probe

[`qlift_doorIV_matrix_crossterm_probe.py`](../../computations/probes/qlift_doorIV_matrix_crossterm_probe.py)
(mpmath dps=70, q ∈ {0.9, 1.05, 1.10998}, m=0..60; fit m=0..20, extrapolate
m=40..60; recessive C1/GGM via Miller from m=200). **Matrix ansatz:** per GGM
solution fit `y_m = a(x)f₊² + b(x)f₊f₋ + c(x)f₋²`, `x=q^m`, `a,b,c` polynomials
in `q^m` of degree ≤4 — the "2×2 GL₂ `M(q^m)` rational in `q^m`" reading, `f₊f₋`
being `M`'s off-diagonal coupler. **Kill:** tail residual `<1e-45` AND
GGM-recurrence residual `<1e-30` ⇒ LANDS; O(1) drift ⇒ REFUTED. Solver self-test
recovers an in-span target to `≤4e-59`, so an O(1) residual is genuine.

## 2. Precondition — MET (the owner's structural fix works)

Measured theta exponent γ (`|·| ~ q^{γm²}`) at substrate **q=1.10998**:

| object | γ | reading |
|---|---|---|
| `f₊` (carrier growing) | **+0.253 ≈ +¼** | slope +½ (growing) |
| `f₋` (forward decaying) | **−0.263 ≈ −¼** | slope −½ (decaying) |
| **`f₊f₋` (cross)** | **−0.010 ≈ 0** | **slope 0 — GATE PASSED** |
| NAIVE both-forward cross | **−0.527** | slope −1 (Door-iii's mis-measurement) |

Slope-0 cross term at every q>1 (q=1.05: −0.025). **For the first time a
C1-derived construction has the right anisoclinic slope multiset {+1,0,−1} to
*contain* GGM {+1,−1}** — Door-i's Newton-polygon (graded-module) obstruction is
genuinely circumvented.

## 3. Verdict — REFUTED (scope-(a))

Despite the correct grading, the tensor-square matrix ansatz does **not**
reproduce any GGM solution: at every q and every target (forward `y_a`,`y_b`;
recessive), the best (degree-0) tail residual is `10⁴⁰–10¹⁸⁴` (O(1)+ drift) and
the reconstruction's GGM-recurrence residual is O(1) (≈0.86–1.10). Higher
polynomial degree overfits the window and extrapolates worse. Crucially
`cross_term_helps = False` at every target: with-cross ≈ no-cross residual — the
slope-0 cross term is *grabbed* by the fit but supplies **no** identifying
power. The intertwiner `M(q^m)` that would map `Sym²/⊗²(C1) → GGM` is **not
rational of low degree**.

**Localization of the remaining gap.** The obstruction has moved: no longer at
the Newton-polygon / slope level (now matched — {+1,0,−1} ⊇ {+1,−1}) but at the
**sub-leading (Stokes / theta fine-structure)** level — the tensor square and
GGM share a graded module yet differ in formal-monodromy data. scope-(a) ("this
construction alone misses"); Door-i owns the module-level (b)-exclusion for C1
itself, which this tensor route was explicitly *outside*.

## 4. Effect on the conjecture + recommendation

`conj:qdifference-kernel-prolongation-symbol` is **unchanged**. Reading **R1**
(C1 / its tensor square is a distinct object from the colored-Jones/Stokes GGM
carrier) is reinforced from a new angle: even after fixing the slope grading via
the carrier lift, the sub-leading Stokes data still separate them. The
anisoclinic-coupler hypothesis is answered: **the slope-0 cross term exists but
is not the connector.** Recommendation: any further tensor-route attempt must
target the **Stokes/theta sub-leading** data directly (e.g. a q-Stokes-matrix
comparison of `⊗²(C1)` vs GGM at the two slopes), not the graded module — that
is now matched.

## 5. Discipline

scope-(a) vocabulary; pre-stated kill criterion + slope-precondition GATE +
solver self-test; NON-module tensor realization by design (Door-i excludes module
maps, explicitly not this route); the only "fit" is the polynomial-coefficient
solve for the kill-test; no AME data. Corpus-grep: the whole C1↔GGM trail is this
branch's 2026-07-20 files; no closed item re-opened. Witness:
[`…doorIV…witness.json`](../../computations/probes/qlift_doorIV_matrix_crossterm_probe.witness.json).
