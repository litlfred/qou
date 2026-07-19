# c₃ and q₀ are the same problem — the self-dual/CS-degeneration locus q\* (three-viewpoint synthesis)

**Date:** 2026-07-19 · **Axis:** 1ppQ closure (c₃/Q_β + q₀-derivation) · **Tier:**
structural synthesis, scope-(a) · **Discipline:** no fit, no c_k wired, nothing to
production, no tier change.

## Origin

Owner asked how to close 1ppQ, to review the bar-odd/c₃ dressing from the **Frobenius
pairing / self-dual / categorical-action** viewpoints, and — sharply — whether the
bar-odd carrier's zero is at a fixed q\* or *at* the pinned q₀ (a circularity check).
Three parallel corpus reviews + the `(N,k)` scan answer all of it.

## The circularity check — fixed q\*, NOT q₀ (but not yet *derived*)

The bar-odd carrier is the figure-eight **Chern–Simons invariant** `Im 𝔙(u)`
(Murakami–Yokota, `math/0401084`), meridian `u(q) = N·ln q − 2πik`
(`computations/qbeta/qbeta_c3_mq0_nk_scan.py`). It is **nonzero at both q₀ pins, with
opposite signs**:

```
S(muon q₀)   = +0.00968298
S(proton q₀) = −0.03945936
q*  (S = 0)  = 1.10997859303   (fixed, 80.3% muon-ward, strictly between the pins)
```

So the zero is at a **fixed geometric q\***, not at the pinned q₀ — **not** the
tautological "zero wherever you measured q₀." **However**, the scan verdict is **0/8**:
no *derived* `(N,k)` winding candidate (icosahedral orders `{3,6,60,120}×{1,2}`)
reproduces the S-values (overshoot 40×–10⁴×; the meridians `|u|≥2π` leave the
figure-eight geometric component, Bloch–Wigner volumes negative/≈0). So **q\* is a
requirement Q_β imposes, not yet a derived categorical constant.** That is the honest
open crux.

## Three-viewpoint convergence (parallel corpus reviews)

**Categorical action.** `c₃ = τ(O)` is a **settled NO**: the "archimedean functor"
factors as the fibre functor τ followed by `π_∞`, a **ring homomorphism into ℝ**
(functor-taxonomy audit `2026-07-11-archimedean-functor-taxonomy.md`); a ring hom of a
smooth object is smooth, so it cannot manufacture the swing. The swing is
**representational** (`~1/u³`, `u = b·ℏ_q²`), pinned by experimental Q_β — scope-(b)
closed against any smooth/functorial source (`2026-07-18-qbeta-odd-channel-cornering-capstone.md`).
The real lead: **q₀-derivation ⟺ the α_EM per-loop measure are the same functorial
problem** — the same `F` on `Jac(Bring)~E⁴`, the same (3,1) isotypic split, the same
`y_λ(1)=(¾,¼)`; both reduce to the **R1 naturality** check ("framework-τ restricts to
the cover-monodromy F"). This is the s5-so3 keystone's own open object.

**Frobenius pairing.** The scalar `Σ_λ y_λ χ_λ` bar-odd carrier is **proved dead**
(`MarkovFrobeniusCollapse` → `S·I`); the Frobenius-Gram *norm* weight is refuted
(`~d_λ²`). The un-taken, codeable route is the **Hilbert–Schmidt matrix pairing**
`⟨O,(G−μ)⁻¹O⟩_HS` — which *sees the 52.8 % off-diagonal* the scalar trace discards, and
is the correct carrier **form**. But a bilinear pairing of two smooth matrices is
smooth: the swing needs the **nonlinear resolvent pole** μ(q), and the only non-fit
source is the geometric Thurston-gluing / Faddeev-Φ_q eval map — **the same open eval
map** the 4₁ ghost-mode probe already defers to. Frobenius re-expresses the carrier
correctly; it does not bypass the geometric dressing.

**Self-dual.** even/odd = meson/lepton = **self-dual/non-self-dual is PROVED at the
object level**: amphichiral 4₁ = Higgs = bar-fixed = real-volume (mass); chiral 5₂ =
non-self-dual = CS/decay (`self-dual-higgs-real-volume.md`,
`electroweak-triplet-charge-spin-from-involution-proof.md`). This confirms the session's
even/odd Stokes finding at the object level. The swing **cannot** be isolated on the
self-dual sector (triply forced: only `±1` phases live there; the diagonal is smooth;
self-conjugate χ is the abelian handle). The one novel lead: the **self-dual-locus
rigidity divergence** — `𝔔_β/Q_A = cos Φ(u)` with `Φ_odd → 0` as `u →` the self-dual
(`u²=1`, CS→0) locus (proved, `phi-b-unitary-bar-odd.md`), so `dΦ_odd/dq` can **diverge
as u is squeezed toward the self-dual face**.

## The synthesis — c₃ and q₀ reduce to one object

The self-dual lens and the scan describe the **same object from two sides**: the CS
carrier vanishing at q\* **is** the self-dual/amphichiral (CS→0) locus, and `dΦ_odd/dq`
diverges there. And q₀ sits right next to q\* (80.3 % muon-ward). Therefore:

> **c₃ (Class A, Q_β/m_n/Δ_pn) and q₀ (Class B, absolute masses) are the same problem** —
> both reduce to **deriving the self-dual/CS-degeneration locus q\***, near which q₀ is
> pinned. The swing is proximity to q\*; q₀'s value is proximity to q\*; the μ–p tension
> is the two pins straddling q\*. The categorical route to *derive* q\* is the
> **F-construction on the Bring/S₅ category (R1 naturality)** — the same `F` the
> cat-action lens independently flagged for q₀ and α_EM.

This does **not** close either: q\* is not yet derived (scan 0/8), and the swing
magnitude stays scope-(b) representational (`1/u³`, experiment-pinned). It **unifies**
the two open problems into one derivation target and names the route.

## Two concrete actionable byproducts

1. **Δ_λ parity bug (self-dual review, scope-(a)).** `delta-lambda-bar-involution.witness.json`
   imposed `Δ_λ = +Δ_{λ'}` (bar-**even**) and got `B_D=−2952 MeV` ("ruled out, wrong sign
   140×"). But the *derived* sign `sgn(λ)=(−1)^{n(λ)}` makes `Δ_λ = sign·dim` **bar-ODD on
   the conjugate pairs** at exactly n=3 (1+/2−) and n=6 (6+/5−) — the min-norm search was
   constrained to the **wrong parity sector**. Re-running Option-E min-norm in the bar-odd-
   on-pairs sector is a clean, un-done check.
2. **Two un-taken codeable probes for the swing:** (i) the **Hilbert–Schmidt matrix-O
   pairing** `⟨O,(G−μ)⁻¹O⟩_HS` with a *derived* geometric pole μ(q); (ii) the **self-dual-
   locus rigidity divergence** — test whether q₀ sits anomalously close to the 5₂
   dressing's self-dual (`u²→1`, CS→0) locus and whether the swing ≈ `1/|u²−1|` (or its
   square root) there. Both consume proved propositions / derived objects, not fitted
   constants — but both hinge on the geometric eval map, which remains the open dressing.

## Scope (anti-laundering)

Synthesizes three corpus reviews + the `(N,k)` scan; answers the circularity check
(fixed q\*, not derived); unifies c₃ and q₀ onto the self-dual-locus derivation; names
the route (F-construction / R1) and two codeable probes. **Closes nothing.** No fit
(any μ(q) or q\* back-solved from Q_β/AME is a fit); no c_k wired; no tier change.
Anti-laundering: axiomatizing `TauRhoHodgeLift` / the F-functor as a §3b class does not
count as deriving q\*.

## Cross-references

- Bar-odd datum is non-abelian: [`2026-07-19-5two-barodd-stokes-majority-nonabelian.md`](2026-07-19-5two-barodd-stokes-majority-nonabelian.md)
- CS-carrier zero q\* + 0/8 winding scan: `computations/qbeta/qbeta_c3_mq0_nk_scan.py`, `qbeta_5two_capstone_carrier_falsification_probe.py`
- Functor taxonomy (τ = fibre functor ∘ π_∞ ring hom): `2026-07-11-archimedean-functor-taxonomy.md`
- Swing is representational (1/u³, scope-(b)): `2026-07-18-qbeta-odd-channel-cornering-capstone.md`
- self-dual = amphichiral = real-volume: `content/.../braids-and-knots/self-dual-higgs-real-volume.md`, `content/.../mass-theory/phi-b-unitary-bar-odd.md`
- q₀ ⟺ α_EM unification (F-construction, R1): `docs/coordination/alpha-em.md`, `docs/coordination/s5-so3-keystone.md`, F T1–T5 audits
- Δ_λ attack-vector map (sign derived; magnitude m<1/√5): `2026-07-18-deltalambda-attack-vector-map.md`
- Ledger: [`docs/coordination/1ppq-qbeta.md`](../coordination/1ppq-qbeta.md)
