# The resurgent/alien-calculus arc under convention D: 45 of 73 audits are C-conditional and none says so

**Date:** 2026-09-06 · **Branch:** `claude/resurgence-conventionD-reanalysis-2026-09-06`
**Beans:** `qou-49vn` (adjacent), this doc's own bean below
**Scope:** measurement + scope-(a) assessment. **No derivation, no number wired, nothing retracted.**
Owner asked: *"Where are we alien calculus and resurgent functions? Some doors may have been
closed due to incorrect compute or on convention C. … Where are the divergent points? Are they
related to saddle points on Brings?"*

---

## 0. The four answers, flatly

1. **The arc is large and live.** 73 audit documents on the resurgence surface
   (`alien|resurg|borel|stokes|gevrey|divergen|transseries|dladder` in the filename), the most
   recent landed 2026-09-05.
2. **The convention-C exposure is real, systematic, and unlabelled.** **45 of the 73** reference
   the `c_k` ladder / `Q_β`, and **zero of them mention convention D**. AGENTS.md states the
   ladder "is convention-C-frame throughout and has not been re-derived" and instructs that every
   `c_k` conclusion be treated as C-conditional. **No audit in this arc carries that scope.**
3. **There are TWO families of divergent point and the corpus does not connect them** (§2).
4. **Yes, there is a Bring-saddle story — and the result built on it is a 1-of-9 selection
   against CODATA** (§3), in a document still advertised as a KEY RESULT.

---

## 1. The C-conditionality measurement

Method: filename filter above over `docs/audits/`; then a tight content regex for a
conclusion-bearing dependence on the ladder (`\bc_3\b|\bc₃\b|\bc_k\b|Q_β|Q_beta|precision
ladder|truncation order`) against `convention[ -]?D`.

| quantity | count |
|---|---|
| resurgence-surface audits | **73** |
| …referencing the `c_k` ladder / `Q_β` | **45** |
| …of those, mentioning convention D | **0** |

Densest dependants (references to the ladder, all with `D = 0`):

| audit | refs |
|---|---|
| `2026-08-09-dladder-is-convergent-radius-is-the-qb-zero.md` | 13 |
| `2026-08-01-qborel-ecalle-resum-barodd.md` | 12 |
| `2026-07-12-borel-alien-calculus-utilization-audit.md` | 11 |
| `2026-07-13-na-stokes-ck-recursion-binding-adversarial-review.md` | 11 |
| `2026-07-17-dladder-ecalle-phib-resummation.md` | 11 |
| `2026-07-12-ohtsuki-symbolic-derivation-borel-phib.md` | 9 |
| `2026-07-17-dladder-parity-split-resummation.md` | 9 |
| `2026-07-18-dladder-fibre-branch-stokes-ambiguity.md` | 9 |
| `2026-08-01-uq0-map-resurgence-surreal-tool-assessment.md` | 9 |

**What this does and does not establish.** It establishes that the arc's conclusions rest on
quantities the repo's own governing document calls C-frame and un-re-derived, and that **not one
of them is scoped as such** — so a reader meeting any of them takes a C-conditional result as
unconditional. It does **not** establish that any particular conclusion is *wrong* under D: that
needs the ladder re-derived, which is `qou-cds1` and is not done here. **Every one of these 45
should carry a C-conditional banner until it is.**

Note also that only **one** file in the arc mentions convention C or `z_C` *by name*
(`2026-08-09-nastokes-orbit-symmetric-readout.md`). The exposure is almost entirely **implicit,
through the ladder** — which is precisely why a grep for "convention C" finds nothing and the
problem looks absent.

---

## 2. Where the divergent points are — two families, unconnected

### 2a. The Borel-plane singularity (analytic)

- The binding kernel's asymptotics are **Gevrey-1/2**, Lean-proved
  (`QOU.Mass.BindingGevreyHalf`). The standard Gevrey-1 Borel plane is therefore the **wrong
  plane**.
- The level-1/2 singularity sits at **`ξ = 1/√2` at `q = 1`**.
- **At `q₀` the class changes to q-Gevrey**, so the correct plane is the **q-Borel plane**
  (Ramis–Sauloy–Zhang theta kernel) and the arithmetic home is the **Habiro ring / cyclotomic
  completion**.
- The archimedean Stokes / wall-crossing structure is **post-`τ`** — the wall the framework
  deliberately does not cross before final evaluation.

Source: [`2026-09-05-alien-calculus-vs-nonabelian-stokes-dialog-assessment.md`](2026-09-05-alien-calculus-vs-nonabelian-stokes-dialog-assessment.md),
[`2026-07-12-alien-calculus-review-binding-gevrey-half.md`](2026-07-12-alien-calculus-review-binding-gevrey-half.md).

### 2b. The colour-cubic discriminant on Bring's surface (geometric)

The colour-tube cubic

```
c³ + (4z+1)c² + (6z²+3z+1)c + (4z³+3z²+2z+1) = 0
```

has discriminant `Δ(z) = -(16z⁶ + 24z⁵ + 35z⁴ + 50z³ + 35z² + 24z + 16)` with **no real roots** —
every critical `z_c` is complex. The pair closest to `z₀ = 0.104` is

```
z_c ≈ 0.106 ± 0.937i
```

and the prolonged SW differential has a severe pole there, where `∂F/∂c → 0`. **A vanishing
derivative is a saddle**, and the route accesses it by a **Picard–Lefschetz thimble** — the
steepest-descent contour from `z_c`.

### 2c. 🛑 The two are NOT connected in the corpus

`ξ = 1/√2 ≈ 0.7071` (Borel plane, level-1/2, at `q = 1`) and `z_c ≈ 0.106 ± 0.937i`
(colour-cubic discriminant, on Bring's surface) live in **different planes with different
coordinates**. I found **no document deriving a map between them**, and none asserting one.

That absence is the most interesting thing in this audit, because the two are *exactly* what
resurgence would relate: Borel singularities are supposed to be the actions of the saddles.
Whether `ξ = 1/√2` is the action of the `z_c` saddle is, as far as this measurement goes, **an
open and apparently unasked question**. Stated as an absence-of-evidence, not evidence-of-absence:
the surface searched was `docs/`, `content/`, `computations/` filename- and content-greps for
saddle∧Bring (38 files) and for the two constants; a derivation living only inside a proof body
or a bean could have been missed.

---

## 3. 🛑 The Bring-saddle result is a 1-of-9 selection against CODATA

[`docs/picard-lefschetz-plan.md`](../picard-lefschetz-plan.md) (last touched 2026-08-10) carries
the status line **"KEY RESULT — simultaneous 3-root product yields m_p to 0.0006%"** and is listed
without caveat in [`docs/README.md`](../README.md).

Its own §"KEY RESULT" section reports **nine prescriptions tested**, with ratios 1.09, 23.5, 0.99,
**2.46**, 1.26, 4.19, 7.74, 366.5, 0 — and marks the fourth **"← WINNER"**. The target is
`A(q₀) ≈ 2.460`, the factor needed for `m_p = Vol(𝔅₃)/ℏ_q² × A × m_e` to land on CODATA.

**That is selection against the target**, which AGENTS.md's NO-FITTING directive names explicitly:

> *"Choosing an object — a knot from a census, a partition, a truncation order, a branch — because
> the choice reproduces the measured value. No continuous parameter is tuned and it is still a
> fit."*

The integration limit `a = (4-q)/(4q+3)` is a second chosen object; the golden-ratio Möbius story
offered for it in `baryon-integration-limit.md` is a rationalisation *after* the choice, not a
derivation *of* it.

**Two further reasons the document should not be read as live:**

1. It targets **absolute `m_p` in MeV**, which the owner ruling of **2026-08-11 — one day after
   this file was last touched — excised**: *"the framework no longer claims, targets, or scores
   an absolute nucleon or atomic mass in MeV as a prediction."*
2. Its accuracy claim (0.0006 %) is exactly the kind AGENTS.md warns ranks *below* an honest
   miss: *"a more accurate fitted route is worth LESS than a less accurate derived one."*

**Nothing here retracts the geometry.** The discriminant locus, the complex `z_c`, the thimble
construction and the `∂F/∂c → 0` pole are structure, and they are the right structure to ask the
§2c question with. What is a fit is the *selection of the prescription* and the *accuracy claim
built on it*.

**Not measured:** whether any downstream artifact consumes `A(q₀) ≈ 2.46`. Twelve other audits
mention `2.46`/`2.4599`; they were not triaged here, and some may be recording the same number
historically rather than using it.

---

## 4. What this recommends (judgement, not finding)

1. **Banner the 45.** A one-line C-conditional scope note on each, or a single note in the arc's
   index that a reader cannot miss. Cheap, reversible, moves no numbers.
2. **Answer §2c** — is `ξ = 1/√2` the action of the `z_c` saddle? It is the question the arc is
   shaped around and appears not to have been asked. This is the door most likely to have been
   closed by accident rather than by argument.
3. **Re-status `picard-lefschetz-plan.md`** — demote "KEY RESULT" to a scope-(a) exploratory
   record, note the 1-of-9 selection and the absolute-mass excision, and keep the geometry.
4. **Do not re-derive the ladder here.** That is `qou-cds1`, it is large, and it gates 1 and 2.

Nothing in 1–3 changes a number; 2 is open research.

---

## 5. §2c is ANSWERED — and by an existing result I should have found first

The §2c question ("is `ξ = 1/√2` the action of the `z_c` saddle?") was posed
above as open and unasked. **It is neither.** The answer lives in
[`2026-09-03-enclosed-pole-set-E-is-not-identifiable.md`](2026-09-03-enclosed-pole-set-E-is-not-identifiable.md)
(bean `qou-qx7j`), three days old when this was written, and my grep missed it
because I filtered audit **filenames** on resurgence vocabulary and that file is
named for its conclusion instead. Recorded because the miss is the reusable part.

### The result

**Every residue of `λ_SW^(n)` vanishes, at every branch point, for every
`n ≥ 1`, independently of the Puiseux data.** Lean `ddz_residue_slot_eq_zero`,
sorry-free, depending on `[propext]` alone.

The mechanism is parity, not cancellation: `λ_SW^(n) = X^(n) dz = X^(n)·2t dt`,
so the residue at a simple branch point is the `t^{−2}` coefficient of a
`z`-derivative — and the only input that could reach that slot is the constant
term, which differentiation kills. Non-vacuity is established in that audit:
`ddz` is not identically zero, and the Puiseux coefficients being killed are
themselves nonzero (`a₀ = −0.07208520691 + 0.6383267351i` at the first branch
point, measured at 60 dps).

Three independent routes reach it — a global primitive (`prop:sw-classical-jet-exactness`),
the compact-surface total residue (`period_eq_zero_of_total_residue_vanishes`),
and this local parity argument, which assumes least.

### What that does to the question

**Sharper than the scope-(a) negative in §3.** `ξ = 1/√2` cannot be the action of
a `z_c` saddle **on the classical-jet prolongation** — not because the
identification is numerically wrong, but because *there is no nonzero action to
compare it to*. My ratio test was measuring against a quantity that is
identically zero.

And it re-scopes `qou-l155` (**pin `λ_SW`**) as **the wrong question as posed**:
pinning `λ_SW` inside the classical jet yields zero however it is pinned. The
live question is upstream — **which prolongation** — and that audit's own
re-scoping says so.

### The convergence — my judgement, not a finding

Both sides of this arc now point at the same place, independently:

- **Borel side** (§2a): the binding kernel is Gevrey-1/2 and **q-Gevrey at
  `q₀`**, so the correct plane is the **q-Borel** plane (RSZ theta kernel) with
  the Habiro ring as arithmetic home.
- **Saddle side** (here): the classical-jet prolongation gives **zero**, and the
  **q-difference prolongation is explicitly untouched** —
  `RamificationParityMonodromy` locates the missing structure as q-jet-bundle /
  q-D-module symbol calculus, absent from both Mathlib and this corpus.

> 🛑 **Scope correction (2026-09-06, bean `qou-p6m1`).** The claim above bundles two objects. The **q-D-module symbol calculus is PRESENT** — `QOU.Machinery.QuantumTorusSymbol` (QDM-1/2, 19 decls, sorry-free, on `main` by 2026-07-24) and `QOU.Mathlib.RamifiedShiftCalculus` (the same calculus at the ramified pole `z = z_c + t²`, sorry-free, 2026-09-03, and it *imports* `RamificationParityMonodromy`, the file that declared it absent). Only the **q-jet bundle over `Σ`** is absent. **W1 (construct `D_q` from `Σ`) still stands** — this is a scoping split, not a downgrade.


Two independent routes arriving at "the classical object is the wrong one; the
q-deformed object is where the content is" is the strongest thing in this
audit. **It is an observation about where two negatives agree, not a derivation**,
and the q-jet machinery it points at does not exist yet in either place.

### Revised recommendation

Recommendation 2 above ("answer §2c") is **withdrawn as stated** — it is
answered. It is replaced by: **do not pin `λ_SW` (`qou-l155`) and do not chase
the thimble action (`qou-p443`) on the classical jet.** The open item is the
q-difference prolongation, and its first obstacle is machinery that has to be
built, not a number that has to be computed.
