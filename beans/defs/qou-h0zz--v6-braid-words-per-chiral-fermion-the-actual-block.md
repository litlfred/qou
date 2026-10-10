---
# qou-h0zz
title: 'V6: braid words per chiral fermion -- the actual blocker for T(t)'
status: todo
type: task
priority: normal
tags:
    - 8f-gen
    - reorg-2026-10-04
    - 8f-open
created_at: 2026-08-10T18:34:14Z
updated_at: 2026-10-10T14:47:10Z
parent: qou-8lxd
---

sm-open-problems.md names this itself: hypercharge Y open, 'framework braid words
per chiral fermion STILL MISSING'.

This is the real blocker, upstream of everything else on the T(t) front. Without a
braid word per chiral fermion there is nothing to read t off, so T(t) is a free
label BY CONSTRUCTION -- which is exactly why the published battery returns a
tautology (TwistBatteryVacuity.lean: the battery collapses to sum(t) = 3Q, and
4 = 1x2x2x1 is multiset counting).

WHAT EXISTS: braid words for the HADRON sector --
  gluon unit        sigma_0 sigma_1^-1      (writhe 0)
  Borromean baryon  B_3 = (sigma_0 sigma_1^-1)^3  (writhe 0)
  Hopf link L_H     from the L+/L- terms
  lepton carriers   e- = T(2,3) trefoil, nu = unknot (KNOT types, not braid words)
WHAT IS MISSING: a braid word per CHIRAL fermion (u_L, d_L, e_L, nu_L and the RH
singlets). The lepton rows are given as knot types only, and chirality is not
represented at all.

NOTE the chirality problem is now sharp (LeptonNumberCarrierChirality.lean): the
carrier cannot be an unframed knot type, so 'e- = trefoil' is not enough -- a
braid word (or framed object) is required for the mirror to act freely.
BLOCKED-BY: V5 (which framing) determines what t even means.


RESULT 2026-08-10 — the braid words are NOT missing; the corpus already fixes them.

chi=-6 constraint: 'T(2,n) with odd n<=7 exhaust the fermion spectrum; electron
T(2,3), neutrino T(2,1)'. And T(2,n) IS the closure of sigma_1^n in B_2. So:
  nu_e = sigma_1^1   (w=+1)      nubar_e = sigma_1^-1 (w=-1)
  e-   = sigma_1^3   (w=+3)      e+      = sigma_1^-3 (w=-3)
  gen2 = T(2,5) = sigma_1^5      gen3 = T(2,7) = sigma_1^7
  baryon B_3 = (sigma_0 sigma_1^-1)^3 (w=0);  gluon unit (w=0)

This RESOLVES the chirality obstruction (LeptonNumberCarrierChirality.lean):
nu and nubar are DIFFERENT BRAID WORDS (w=+1 vs -1) though both close to the
unknot. The mirror acts freely at braid level exactly as predicted.

CANDIDATE FOUND: L(beta) = sign(writhe(beta)), parameter-free, matches 6/6
corpus rows (both leptons, both antileptons, baryon, gluon unit). Consequence:
Y = B - L closes all four LH rows (u,d = 1/3; nu,e = -1).
computations/chiral_fermion_braid_words_probe.py

NOT A CLOSURE -- three caveats:
 1. sign() is a CHOICE of function, not derived from the framework.
 2. The QUARK braid word is still NOT in the corpus; w=0 is ASSUMED (motivated by
    the gluon unit being writhe-balanced). Every quark row rests on it.
 3. Chirality L vs R is still unrepresented -- no distinct word for u_L vs u_R.

KEY CONSEQUENCE for the writhe-independence tension: L = sign(w) is
writhe-DEPENDENT, and that is FINE. Y = B - L still does not factor through w
because B varies at fixed w. So the 'second invariant independent of the writhe'
is B (mu-bar_123), NOT L. The apparent L-needs-framing vs Y-needs-independence
collision dissolves: L needs the BRAID WORD (which carries writhe), not a free
framing datum.


---

## 🛑 SCOPE CORRECTION — the LEPTON half of this is already derived, sorry-free, and verified (2026-10-10)

This bean's title calls braid words per chiral fermion *"the actual blocker for
T(t)"*. That is **half true as of 2026-08-17** and the other half is on a
**`scrapped`** bean, which is why it keeps being reported as wholly open — I did
exactly that in four places today before reading it.

**The carrier is `htw2`** (`beans/defs/htw2--gap-per-chiral-fermion-framed-braid-words-for-strand-twist-total.md`,
294 lines, status **`scrapped`** as a duplicate of `qou-kebu` in the 2026-10-04
reorg). Its *content* was never retracted — only the work item was closed — and
the §path-6 rule about reading `scrapped` beans is exactly what finds it.

### What is DERIVED (not enumerated), verified on `main` `3c0351a40da` today

A framed braid word **does** exist for the leptons, from the corpus's own
`knot-particle-dictionary.md:4` (*"Fermions (n odd) are KNOTS (1 component) …
Quarks are Borromean-linked unknots"*):

    beta_nu = sigma1 sigma2  in B_3,  framing t = (0,0,0)

its closure is the unknot — one component, transitive permutation — so
component-constancy forces a **constant** framing and the pinned total fixes the
value.

| decl | file | gives |
|---|---|---|
| `lepton_framing_determined` | `ComponentFraming.lean` | transitive π + total 3Q ⟹ `t ≡ Q` |
| `nu_framing_is_zero` | same | `Q = 0` ⟹ ν = `{0,0,0}` |
| `nu_distinct_multiset_excluded` | same | a knot closure cannot carry an injective framing ⟹ `{-1,0,1}` **refuted**, and this needs no total at all |
| `e_framing_is_neg_one` | same | e = `{-1,-1,-1}`, derived |
| `d_multiset_forced` | `SignCoherentTwist.lean` | range + total −1 + coherence ⟹ `{-1,0,0}` |
| `coherent_iff_all_same_sign` | same | coherent ⟺ all ≥ 0 or all ≤ 0 |
| `cancel_preserves_total` | same | the reduction step fixes the total |

**Verified rather than taken on trust**, since a bean is not a primary source:
`lean -DautoImplicit=false -s 65536` on both files → **rc=0, 0 diagnostic
lines** (status captured directly, not through a pipe); `ComponentFraming.lean`
304 lines, `SignCoherentTwist.lean` 226 lines, and **0 `sorry` / 0 `axiom` /
0 `native_decide`** in each. All 7 declarations above resolve by name.

**And sign-coherence is no longer an import.** `htw2`'s own later section
upgrades it: because the twist axiom forces `θ_V = q^{1/2}·id_V` on the defining
representation, `θ_V ⊗ θ_V⁻¹ = id` **as morphisms**, so a `(+1,−1)` strand pair
is *ribbon-invisible* and cancelling it rewrites the same state rather than
choosing a different one. The two survivors sign-coherence excludes are the
**un-reduced spellings** of the two it keeps (`d {-1,-1,1} → {-1,0,0}`,
`ν {-1,0,1} → {0,0,0}`). So the residual went **1·2·2·1 → 1·1·1·1**.

### What is STILL OPEN — and this is what this bean should carry

1. **The TOTAL twist is pinned by the SM target**, `T = 3Q`, not computed. `htw2`
   item 1 says so explicitly and nothing above changes it. Deriving `Q(f)` for an
   individual chiral fermion is the real open object; the framework's derived
   `Q = w/2` is a **hadron-level** result and assigns no writhe to a single
   chiral fermion.
2. **The quark side is CONSISTENT, not derived.** Identity-π on the 3-component
   Borromean braid *leaves* `{0,1,1}` available — a transitive π would have
   killed it — which is a real cross-check that passes, and is not a derivation.
3. **Chirality is untouched** — that is `qou-wqto`, and no braid word
   distinguishes `u_L` from `u_R`.
4. **The `1/3` normalisation** (`Q_twist = T/3`) is still the Bilson-Thompson
   helon precedent, not derived.
5. `conj:sm-hypercharge-invariant` stays **open**, and per rule 13a nothing here
   closes it.

### The reusable lesson, because it is the epic's own rule unapplied

The epic `qou-8lxd` records: *"before working a bean, read the beans it cites AND
the beans that cite it."* I wrote that rule after measuring that 5 of 13 bodies
across two fronts were stale against a sibling bean — and then recommended
`htw2` as "the root blocker, highest leverage" **without opening it**, four times,
on the strength of its title. A `scrapped` bean with 294 lines of verified
sorry-free Lean is the sharpest form of that trap: the status says "ignore me"
and the body holds the answer.
