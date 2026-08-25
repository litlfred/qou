# α_EM R2 Quillen-curvature attack — $1/(8\pi)$ as a determinant-line curvature coefficient: shape-compatible, selection-dependent, NOT derived

**Date:** 2026-07-25 · **Bean:** qou-jkcx · **Axis:** α_EM per-loop measure (R2) /
Bring Jacobian family / Quillen curvature · **Tier:** scope-(a), audit-only ·
**Discipline:** DERIVATION-ONLY; the owner ruling stands
([`2026-07-19-alpha-em-r2-owner-ruling.md`](2026-07-19-alpha-em-r2-owner-ruling.md)):
R2 is **not** Lean/derived-proved; $1/(8\pi)$ stays a phase-4 identification;
**NOTHING wires regardless of outcome**. NO FIT.

**Probe:** [`computations/probes/alpha_em_r2_quillen_curvature_probe.py`](../../computations/probes/alpha_em_r2_quillen_curvature_probe.py)
→ [`alpha-em-r2-quillen-curvature-probe.witness.json`](../../computations/probes/alpha-em-r2-quillen-curvature-probe.witness.json)
— 6/6 assertions passed, exit 0; every candidate compared to $1/(8\pi)$ in exact
rational arithmetic (no tolerance).

**What this executes:** the §5 proposal of the merged
[Quillen anomaly classification](2026-07-25-quillen-anomaly-classification.md) —
test whether the per-loop normalization $1/(8\pi)$ arises as a **curvature
coefficient** of a determinant line bundle over the framework's own family (the
derivable class), rather than as a norm point-value (the class every prior
magnitude probe evaluated and failed on).

## 0. Distinct-angle coordination note

The active B2 sibling cluster on `main` this week — `a2ee67bd`
(`MatrixSchurCommutant`), `1a83135b` (Hodge-side normalization probe),
`58c3d52f` (sub-piece (ii): equivariance ⇒ τ(Markov)∝Hodge, conditional), the
PR #4182/#4168 lineage — attacks the **identification** "loop weight = Hodge
Gram" *algebraically* (Schur commutant, invariant-form proportionality,
equivariance). This tranche attacks the **normalization** $1/(8\pi)$
*geometrically*, as a curvature coefficient over the Bring Jacobian family. The
two routes are complementary and share no files; the parent posts intent on the
sibling PR.

## 1. The exact target object (Task 1 — written down before computing)

After the 2026-07-19 decomposition
([`2026-07-19-alpha-em-r2-decomposition.md`](2026-07-19-alpha-em-r2-decomposition.md),
[`…-r2core-schwinger.md`](2026-07-19-alpha-em-r2core-schwinger.md),
[`2026-07-25-alpha-em-b2-tau-id-consolidation.md`](2026-07-25-alpha-em-b2-tau-id-consolidation.md)),
R2's surviving open content is exactly:

1. **R2-core** — *"the loop expansion weighs proper time by the standard
   Schwinger measure with unit normalization — one per-mode unit on the doubled
   pair"* (one unit convention + the $\tfrac12$-adjudication: proper-time vs
   energy e-folds);
2. **the B2 τ-identification** — equivariance + the scalar $c$ (the sibling
   cluster's front).

The working coefficient is $\tfrac12 \cdot a_0 = 1/(8\pi)$ with
$a_0 = 1/(4\pi)$ the 2D heat-kernel unit (derived, #3909); the count $b_1 = 8$
is proved (#2114/#3834/#3896); the entire underived residual is the single
$\tfrac12$ (#3925).

**Mismatch finding (reported, not forced).** R2-core's object is a
**proper-time measure normalization** — *not* a determinant-line point value or
curvature. The task anticipated this possibility, and it is real: the Quillen
proposal does not aim at R2's object directly. What makes the curvature attack
meaningful anyway is the **Bismut–Freed bridge**: the Quillen curvature of the
determinant line is computed by the *same heat-kernel index density* (AGMV
Sect. 4, below Eq. (4.18)) that produces $a_0$. So the candidate identity class
is a **shape test**:

> $1/(8\pi) \stackrel{?}{=}$ (curvature coefficient of a determinant line $L$
> over the Bring family, extracted against the scale-invariant reference form,
> normalized by a framework-forced count),

with every ingredient named per candidate. If every match requires an unforced
ingredient, the honest verdict is pre-declared: *shape-compatible,
selection-dependent — not derived.*

**The named ingredients (common to all candidates):**

- **Family:** $\mathrm{Jac}(\mathrm{Bring}) \cong E_{5\tau}^3 \times E_\tau$
  (complex torus, not ppav; $\tau_B = \tau_0 M_{RR}$,
  $\mathrm{spec}(M_{RR}) = \{5,5,5,1\}$ ⇒ factor multiplicities $(3,1)$ —
  BN12/BDH22 data verified exactly in
  [`tau_dictionary_fricke_spin_probe.py`](../../computations/probes/tau_dictionary_fricke_spin_probe.py)),
  one-parameter base $\tau \in \mathbb{H}$ through the Bring point
  $\tau_0 = -\tfrac12 + 0.186676i$, fibres $(5\tau, 5\tau, 5\tau, \tau)$.
- **Operator:** $\bar\partial$ per elliptic fibre — equivalently the scalar
  Laplacian via the verified
  $\det{}'\Delta(E_\tau) = (\mathrm{Im}\,\tau)^2 |\eta|^4$; for the
  spin-content candidates, the AGMV family $D: L^n \to L^{n+2}$ with
  obstruction weight $3(n+1)^2 - 1$ (AGMV Eqs. (4.25)–(4.32)). **Spin
  structure:** the $S_5$-invariant characteristic is the **even/Szegő** one
  (A6, forced — the unique fixed point of $S_5$ on the 256 characteristics,
  [`2026-07-24-tau-dictionary-fricke-cusp-spin.md` §3](2026-07-24-tau-dictionary-fricke-cusp-spin.md));
  per AGMV (below Eq. (4.32)) $S_L$ and $U_{\mathrm{WP}}$ make **no reference
  to the characteristic**, so the forced spin structure is
  curvature-coefficient-blind — it cannot carry the $\tfrac18$.
- **Measure:** coefficient extraction against
  $\omega_{\mathrm{hyp}} = dx \wedge dy / y^2$ — both the curvature form and
  $\omega_{\mathrm{hyp}}$ are invariant under $\tau \mapsto 5\tau$ (verified
  exactly), so the extraction is well-defined along the family; for the
  Belavin–Knizhnik candidates, AGMV's WP normalization (4.31):
  $\delta\bar\delta W = -\tfrac{3(n+1)^2-1}{64\pi}\,\langle \delta g, \delta g\rangle_{\mathrm{WP}}$.

**Building block (exact).** From the merged classification's curvature
$\partial_\tau\partial_{\bar\tau} \log \det{}'\Delta(E_\tau) = -1/(2\,(\mathrm{Im}\,\tau)^2)$
and AGMV's (4.18) normalization $\tfrac{i}{2\pi}\partial\bar\partial \log \lVert\sigma\rVert^2$,
using $d\tau \wedge d\bar\tau = -2i\, dx \wedge dy$:

$$
c_1(L_\tau) \;=\; -\frac{1}{2\pi}\,\omega_{\mathrm{hyp}}
\qquad \text{(exact; per elliptic factor)} .
$$

Sign recorded: the curvature is negative, as is the working loop insertion in
$[2]_q(1 - h^2\alpha)$; magnitudes are compared below.

## 2. The candidate table (Task 2 — exact values, rational comparison)

All values exact rational $\times\,1/\pi$; ratio = candidate $\div\, 1/(8\pi)$,
computed in sympy rational arithmetic. $\kappa = 1/(2\pi)$ is the per-factor
curvature magnitude; $b_1 = 8$; $g = 4$; $a_0 = 1/(4\pi)$.

| Key | Candidate identity | Exact value | Ratio | Verdict |
|---|---|---|---|---|
| T0 | $1/(\pi \cdot b_1)$ — the PR #1552 phase-4 identification itself | $1/(8\pi)$ | $1$ | **tautology floor** (definitionally the thing to be derived; not a candidate) |
| Q-A | product line, unit multiplicities $(1,1,1,1)$: $4\kappa$ | $2/\pi$ | $16$ | **MISS** |
| Q-A5 | isogeny-degree weights $(5,5,5,1)$: $16\kappa$ | $8/\pi$ | $64$ | **MISS** |
| Q-B | per-real-cohomology-mode: $4\kappa / b_1$ | $1/(4\pi) = a_0$ **exactly** | $2$ | **MISS by exactly 2** — structural corroboration (§3) |
| Q-C | per-mode on the complexified doubled pair: $4\kappa / (2 b_1)$ | $1/(8\pi)$ | $1$ | **MATCH — selection-dependent** |
| Q-D | Belavin–Knizhnik WP coefficient, scalar content: $\sum_i [3(n_i{+}1)^2{-}1] = 4\cdot 2 = 8$, then $8/(64\pi)$ | $1/(8\pi)$ | $1$ | **MATCH — selection-dependent** |
| Q-E1 | photon spin-1 content, $n=2$: $4 \cdot 26/(64\pi)$ | $13/(8\pi)$ | $13$ | **MISS** |
| Q-E2 | photon content, $n=1$: $4 \cdot 11/(64\pi)$ | $11/(16\pi)$ | $11/2$ | **MISS** |

**Prune (formalize-first):** $3(n+1)^2 - 1 = 8 \Rightarrow (n+1)^2 = 3$ has no
integer solution (asserted) — **no single AGMV spin weight equals 8**; only
sums can reach 8, and the only structurally-suggested sum that does (four
scalar factors, Q-D) equals $2g = b_1$, the count in disguise.

## 3. The one genuinely new derived-shape result (from forced legs only)

**Q-B: the Quillen route independently reproduces $a_0$.** Using only forced
ingredients — 4 factors ($g=4$, $\mathrm{spec}(M_{RR})$), the per-factor
curvature $-1/(2\pi)$ (this probe + AGMV (4.18)), and the proved count
$b_1 = 8$ — the per-real-mode curvature coefficient is

$$
\frac{4 \cdot \tfrac{1}{2\pi}}{b_1} \;=\; \frac{1}{4\pi} \;=\; a_0
\qquad \text{(exact)} ,
$$

the derived heat-kernel unit of #3909, now reached through the
determinant-line geometry instead of the proper-time Gaussian. The residual
against the target is **exactly $2$** — the same single open $\tfrac12$ that
#3925 located between the derived $1/(4\pi)$ and the data $1/(8\pi)$. Two
independent machineries (Schwinger heat kernel; Quillen/Bismut–Freed
curvature) now agree on both the derived unit *and* the location of the wall.
This is corroboration of the wall's position, **not** progress through it —
consistent with the Bismut–Freed bridge being the same index density.

## 4. Tautology audit (Task 3 — mandatory, per matching candidate)

Forced framework facts available to candidates (each independently cited):
the 4 factors and $(3,1)$ multiplicities ($\mathrm{spec}(M_{RR}) = \{5,5,5,1\}$,
BN12/BDH22, verified exactly); $b_1 = 8$ (proved, #2114/#3834/#3896);
$a_0 = 1/(4\pi)$ (adjudicated, #3909); the Hodge doubling
$H^1 \otimes \mathbb{C} = H^{1,0} \oplus H^{0,1}$ (#3920); the even/Szegő
invariant characteristic (A6, unique $S_5$ fixed point); the per-factor
curvature $-1/(2\pi)$ (this probe + AGMV (4.18)).

| Match | Unforced choice it needs | Was it selected because it lands on 8? |
|---|---|---|
| **Q-C** ($4\kappa/16$) | the divisor $16 = \dim_\mathbb{R}(H^1(M,\mathbb{R}) \otimes \mathbb{C})$ — counting per **real** dimension of the **complexified** pair space | Yes, effectively: no independent framework fact selects this count over Q-B's $b_1 = 8$. Counting per unit of the doubled pair **is verbatim the R2-core premise** ("one per-mode unit on the doubled pair"). Q-C does not derive R2 — it *restates* it in curvature language. |
| **Q-D** ($8/(64\pi)$) | (i) scalar operator content $n=0$ per factor — the framework's photon lives on real 1-forms (spin-1 content gives $13/(8\pi)$ or $11/(16\pi)$, both MISS); (ii) AGMV's $/(64\pi)$ WP normalization convention | Yes on (i): the scalar choice is the unique small spin content whose weight sum lands on 8, and no independent framework fact forces scalars on the Jacobian factors. Moreover $\sum = 4 \cdot 2 = 2g = b_1$: the "match" is the $b_1$ count re-entering through the weight formula — the T0 tautology in Belavin–Knizhnik clothing. And (ii): WP inner-product normalizations vary by convention; the exact landing inherits AGMV's. |

Every candidate built from **forced ingredients only** (Q-A, Q-A5, Q-B, Q-E)
**misses** — by $16$, $64$, $2$, $13$, $11/2$ respectively.

## 5. Verdict

**Shape-compatible, selection-dependent — not derived.** The classification's
§5 proposal is *half*-vindicated: $1/(8\pi)$ does sit comfortably in the
curvature-coefficient class (exact rational $\times\,1/\pi$ landings exist,
unlike every norm point-value probe, which produced non-distinguished reals),
and the curvature machinery independently re-derives $a_0$ and re-locates the
known open $\tfrac12$ (§3). But **no candidate derives $1/(8\pi)$ from forced
ingredients**: each exact match consumes exactly one unforced discrete choice,
and in both cases that choice is a *restatement of R2's already-known open
content* (Q-C ↔ the R2-core per-mode-on-the-pair premise; Q-D ↔ the
reciprocal-$b_1$ identification, plus a WP convention). The Quillen attack
therefore **relocates the wall without breaching it** — exactly the honest
outcome the owner ruling anticipated: no amount of consistency checking makes
R2 proved.

Secondary findings, recorded:

- **Mismatch finding (§1):** R2-core's object is a Schwinger proper-time
  measure normalization, not a determinant-line quantity; the curvature
  framing is a shape test via the Bismut–Freed bridge, not a direct attack on
  R2's object. Any future "curvature derivation" claim must first close this
  object-level gap.
- **Spin-structure blindness:** the forced even/Szegő characteristic cannot
  carry the $\tfrac18$ (AGMV: $S_L$, $U_{\mathrm{WP}}$ reference no
  characteristic) — pruning one tempting "use the A6 result to pick the
  factor" route.
- **No single AGMV spin weight is 8** ($(n+1)^2 = 3$ insoluble over
  $\mathbb{Z}$) — the only route to 8 through the spin-weight formula is a
  sum, and the natural one is $2g = b_1$ in disguise.

**Nothing wires.** The verdict goes to the owner; $1/(8\pi)$ remains phase-4;
all scope labels are (a) — the misses refute the *stated candidates only*.

## 6. Scope discipline (anti-laundering)

- **NO FIT.** Candidates were enumerated from the family/operator/measure
  structure before comparison; none was adjusted toward $1/(8\pi)$; all
  comparisons are exact rational (no tolerance). The two matches are reported
  *with* their unforced choices named, per §Before declaring "refuted" /
  the tautology-audit mandate — neither is claimed as a derivation.
- **Scope-(a) throughout.** Each MISS refutes its stated candidate identity
  only. The spin-weight prune cites an exact arithmetic invariant
  ($(n+1)^2 = 3$ insoluble); the spin-structure blindness cites AGMV's own
  statement.
- **Nothing wired; audit-only witness** (`set_audit_only`); no production
  script, dashboard, or content block touched; the owner ruling's guardrails
  are intact.
- **Render-QA:** the preflight grep battery was run by hand (balanced
  `$`/`$$`/braces, no `\operatorname`, no markdown-list hijack lines inside
  display math, no inline align-family environments); the pipeline render was
  not run in this sandbox — stated explicitly per the render-QA gate: this
  change was not machine-validated.

## 7. Cross-references

- Owner ruling (read-first): [`2026-07-19-alpha-em-r2-owner-ruling.md`](2026-07-19-alpha-em-r2-owner-ruling.md)
- R2 decomposition / R2-core: [`2026-07-19-alpha-em-r2-decomposition.md`](2026-07-19-alpha-em-r2-decomposition.md), [`2026-07-19-alpha-em-r2core-schwinger.md`](2026-07-19-alpha-em-r2core-schwinger.md)
- The §5 proposal executed here: [`2026-07-25-quillen-anomaly-classification.md`](2026-07-25-quillen-anomaly-classification.md) + [`quillen_anomaly_classification_probe.py`](../../computations/probes/quillen_anomaly_classification_probe.py)
- The $\tfrac12$ wall location: `2026-07-18-alpha-em-reciprocal-form-consolidation.md`; π-origin: `2026-07-18-alpha-em-pi-origin-adjudication.md`
- B2 sibling cluster (distinct angle, §0): `MatrixSchurCommutant` (`a2ee67bd`), Hodge normalization (`1a83135b`), equivariance reduction (`58c3d52f`), [`2026-07-25-alpha-em-b2-tau-id-consolidation.md`](2026-07-25-alpha-em-b2-tau-id-consolidation.md)
- Bring Jacobian / spin data: [`2026-07-24-tau-dictionary-fricke-cusp-spin.md`](2026-07-24-tau-dictionary-fricke-cusp-spin.md)
- AGMV upload: `library/alvarez-gaume-moore-vafa-1986-theta-functions-modular-invari/alvarez-gaume-moore-vafa-1986-theta-functions-modular-invariance-and-strings.pdf` (Commun. Math. Phys. **106**, 1–40 (1986)), Sect. 4 Eqs. (4.1)–(4.2), (4.4)/(4.6), (4.17)–(4.18), (4.25)–(4.27), (4.30)–(4.32)
- Ledger: [`../coordination/alpha-em.md`](../coordination/alpha-em.md)
