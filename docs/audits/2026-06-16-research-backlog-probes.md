# Research-backlog feasibility probes — 2026-06-16

Formalize-first probes against the four open items in
`.beans/paper-todos.json` that the author prioritized this session
(items #7, #6, #4, #1 in the session triage table). Each probe was run
**before** committing to any wide/expensive search, per CLAUDE.md
*"Formalize-first probe discipline"*.

Reproducible compute:
[`folio-assistant/computations/research_backlog_probes_2026_06_16.py`](../../folio-assistant/computations/research_backlog_probes_2026_06_16.py)
→ [`research-backlog-probes.witness.json`](../../folio-assistant/computations/research-backlog-probes.witness.json).

| Item | Block | Verdict |
|------|-------|---------|
| #1 | `cl3-zeta5-geometric-realization` | **smallest-viable-step is ill-posed** (refuted) |
| #7 | `negative-debt-confinement` | **route closed**: tractable, but colour resolution is trace-invisible (singlet $\dim_q=1$) and the entanglement escape is blocked by confinement (1-dim colour block) — $\mathfrak{E}_0$ cannot come from colour |
| #6 | `gram-matrix-h3-symbolic` | **deferral confirmed correct** (brute-force re-checked) |
| #4 | `bigbang-heatdeath` | speculative metaphor; no action (math already correct) |

---

## #1 — cl3-zeta5: the proposed CS computation cannot discriminate

The bean's "smallest viable next step" reads:

> numerical SnapPy CS computation on the seven Bring-natural
> torus-knot generators
> $\{T(2,3), T(2,5), T(2,7), T(2,9), T(3,4), T(3,5), T(5,2)\}$,
> fit the resulting numbers as $\mathbb{Q}$-linear combinations of
> $\{\zeta(3), \mathrm{Cl}_3(2\pi/5), \mathrm{Cl}_3(2\pi\cdot 2/5)\}$
> and report which torus knot has the cleanest match.

Run (SnapPy 3.3.2, census names $3_1, 5_1, 7_1, 9_1, 8_{19}, 10_{124}$):

| generator | census | hyperbolic? | volume | Chern–Simons |
|-----------|--------|-------------|--------|--------------|
| $T(2,3)$ | $3_1$ | **no** | $0$ | $-1/12$ |
| $T(2,5)$ | $5_1$ | **no** | $0$ | $1/20$ |
| $T(2,7)$ | $7_1$ | **no** | $0$ | $3/28$ |
| $T(2,9)$ | $9_1$ | **no** | $0$ | $5/36$ |
| $T(3,4)$ | $8_{19}$ | **no** | $0$ | $1/24$ |
| $T(3,5)$ | $10_{124}$ | **no** | $0$ | $2/15$ |
| $T(5,2)$ | $5_1$ | **no** | $0$ | $1/20$ |

**Every generator is a torus knot, hence Seifert-fibered and
non-hyperbolic** (SnapPy reports volume $0$, "contains flat
tetrahedra"). Their Chern–Simons invariants are therefore **rational
numbers** — exactly the framing-corrected CS of the Seifert structure,
with **zero** transcendental content.

The fit target $\{\zeta(3), \mathrm{Cl}_3(2\pi/5),
\mathrm{Cl}_3(4\pi/5)\}$ is a basis of **irrational/transcendental**
weight-3 periods. A rational CS value has a trivial (zero) projection
onto this basis. So:

> **The proposed discriminating computation cannot discriminate.** There
> is no Cl₃/ζ(3) signal to read off torus-knot CS, because torus knots
> carry no hyperbolic weight-3 period.

This matches the standing CLAUDE.md warning (KLR/crystal audit,
2026-05-30): *"Bloch–Wigner / dilog-transcendence arguments on the
trefoil (non-hyperbolic → D(z) = 0)"* — the same degeneracy at weight 2,
here re-confirmed at weight 3.

**Redirected next step.** A meaningful cl3-zeta5 probe needs
**hyperbolic** 3-manifolds Bring-naturally tied to the quintic — e.g. the
icosahedral hyperbolic orbifold / the quintic's monodromy representation
— where CS pairs with a non-zero hyperbolic volume into a genuine complex
weight-3 period. Torus-knot complements are the wrong test objects. This
does not resolve item #1 (still "the deepest unsolved problem"), but it
removes a blind alley from its roadmap.

---

## #7 — negative-debt-confinement: the 9-strand direction is compute-tractable

The bean frames the 9-strand $H_9(q)$ direction as gated by raw size:

> the Gröbner–Shirshov basis for $H_9(q)$ has $9! = 362{,}880$ terms …

But the physical observable is the **Markov trace** $\mathrm{tr}_M$ of the
(closed) nucleon braid, and $\mathrm{tr}_M$ is a **Wedderburn character
sum** over the irreducible blocks of $H_9(q)$ — not a $9!$-term normal-form
enumeration. The $9!$ figure is the dimension of the *regular*
representation, not the cost of a trace.

H₉ Wedderburn data (instant, $0.06$ s):

- **30 irreps** (partitions of $9$),
- $\sum_\lambda (\dim V_\lambda)^2 = 362{,}880 = 9!$ (consistency check),
- **max irrep dimension $216$**; dims
  $\{216, 216, 189, 189, 168, 168, 162, 162, 120, 120, 105, \dots\}$.

Evaluating $\mathrm{tr}_M(\mathcal{B}_9)$ via the Hoefsmit/Wedderburn
route is a sum of $30$ block characters, each on a matrix of dimension
$\le 216$ — entirely feasible with the existing `pyhecke` /
`hecke-engine` infrastructure (the same route already used at $H_3$).

> **Reframe:** #7 is **not** blocked by compute scale. The real gate is
> *defining* the color-resolved 9-strand nucleon braid word (3 quarks ×
> 3 colors, closing to a 9-strand Borromean link) and the
> energy-extraction map from its trace to $\mathfrak{E}_0$.

That definition is a **modeling decision**, not a calculation — and a
load-bearing one: inventing a 9-strand word and then "predicting"
$\mathfrak{E}_0 \approx 4.155$ MeV from it would be exactly the post-hoc
fit the three-calibration discipline and the critical-distance license
warn against. The honest path is to fix the braid word from an
independent structural principle (color-singlet closure + the existing
$u$–$d$ crossing-typing of the $H_3$ model) **first**, then compute
$\mathrm{tr}_M$ and check $\mathfrak{E}_0$ as a genuine prediction.

### #7 next step — the literal color-resolution is trace-invisible

Carrying out the principled construction the author approved (resolve
each quark into a 3-strand color bundle; close on the baryon
color-singlet; keep the $u$–$d$ flavor typing), a structural obstruction
appears **before** any braid word need be written down.

A baryon is a color singlet: totally **antisymmetric** in the three
quark colors ($\varepsilon_{abc}$), i.e. the **$(1^3)$** irrep of the
color $H_3(q)$. If the 9 strands factor as colour $\otimes$ flavour
(the clean, freedom-free reading of "tensor each quark with its colour
bundle"), the Markov trace factorises and the colour contribution is the
**quantum dimension of the closed colour channel**:

$$
\mathrm{tr}_M(\mathcal{B}_9) \;=\; \mathrm{tr}_M(\mathcal{B}_3)\;\cdot\;\dim_q(1^3).
$$

But $(1^3)$ is a single column (hooks $3,2,1$), so

$$
\dim_q(1^3) \;=\; \frac{[3]_q!}{[3]_q[2]_q[1]_q} \;=\; 1 \qquad\text{identically, for all } q
$$

(sympy-verified exact; numerically $1.000000$ at $q_0 = 1.10998$; by
contrast the standard channel $\dim_q(2,1) = q + q^{-1} = [2]_q \approx
2.0109$).

> **Verdict (#7).** The literal "each quark → 3-strand colour bundle,
> closed on the colour singlet" construction is **trace-invisible**:
> $\mathrm{tr}_M(\mathcal{B}_9) = \mathrm{tr}_M(\mathcal{B}_3)$, because
> the antisymmetric colour singlet has quantum dimension exactly $1$. It
> **reproduces** the $H_3$ result and therefore predicts **nothing new**
> about $\mathfrak{E}_0$ — the energy scale stays a calibration.

The only way to make the 9-strand trace carry $\mathfrak{E}_0$-fixing
information is to **break the colour$\otimes$flavour factorisation** —
entangle the colour and flavour braidings so the closure is no longer a
pure $(1^3)$ projector. This "entanglement escape" is scoped below.

### #7 entanglement escape — closed by confinement (1-dim colour block)

One refinement is needed first: a 1-dim block is *not* automatically
trace-invisible for a **non-trivial** colour braid. On a 1-dim irrep each
generator $\sigma_i$ acts as a *scalar eigenvalue*, so a non-trivial
colour word (e.g. the Borromean closure $(\sigma_1\sigma_2^{-1})^3$ the
bean invokes) could in principle contribute a $q$-power, not $1$. We check
it.

Action of the **Borromean colour word $(\sigma_1\sigma_2^{-1})^3$** on each
$H_3(q)$ irrep (explicit 2-dim seminormal rep, braid relation residual
$=0$, Hecke relation $(\sigma-q)(\sigma+q^{-1})=0$ verified):

| colour block | physical role | $(\sigma_1\sigma_2^{-1})^3$ acts as |
|--------------|---------------|--------------------------------------|
| $(3)$ trivial | — | scalar $\mathbf{1}$ |
| $(1^3)$ sign | **baryon colour singlet** | scalar $\mathbf{1}$ |
| $(2,1)$ standard | colour **octet** (non-singlet) | **non-scalar**, $\operatorname{tr} = -q^6+3q^4-3q^2+4-3q^{-2}+3q^{-4}-q^{-6} \approx 1.994$ at $q_0$ |

On **both** 1-dim blocks the Borromean word is the scalar $1$ — by
**eigenvalue cancellation**: each $\sigma$ contributes its eigenvalue $e$,
each $\sigma^{-1}$ contributes $e^{-1}$, and the balanced word
$(\sigma\sigma^{-1})^3$ collapses to $e^0=1$ regardless of $q$ or of which
eigenvalue ($q$ on $(3)$, $-q^{-1}$ on $(1^3)$). This is robust to *any*
crossing-balanced colour word, and a colour-singlet closure is balanced.

> **Verdict (#7 entanglement escape — CLOSED).** Colour **confinement**
> forces the baryon colour sector into the 1-dimensional sign irrep
> $(1^3)$. On a 1-dim block every colour braid acts as a *scalar*, and the
> balanced (Borromean) colour word acts as exactly $1$. The only block
> where the colour braid carries non-trivial trace information is the 2-dim
> standard $(2,1)$ — the colour **octet**, which confinement strictly
> forbids a baryon to occupy. So colour–flavour entanglement is **neither**
> an independent structural fix **nor** a tunable free parameter for
> $\mathfrak{E}_0$: the 1-dimensionality of the confined colour singlet
> closes *both* doors.

**Net result for #7.** The "9-strand $=$ 3×colour predicts
$\mathfrak{E}_0$" hypothesis is **closed as a viable route**:

- trivial colour (identity): factor $1$ (trace-invisible),
- Borromean colour closure: still factor $1$ on the $(1^3)$ singlet
  (eigenvalue cancellation),
- colour–flavour entanglement: blocked — confinement pins colour to a
  1-dim irrep, whose scalar action carries no $\mathfrak{E}_0$ knob.

$\mathfrak{E}_0$ therefore **cannot** come from colour resolution; it must
originate in the flavour/spatial sector (the existing $H_3$ $u$–$d$ typing
+ spatial braiding) or from genuinely new structure. This still does not
*derive* $\mathfrak{E}_0$ — it remains a CAL-style calibration — but it
removes the entire colour-resolution programme from its roadmap, replacing
a multi-day $H_9$ compute with a one-line representation-theoretic
argument (formalize-first). Reproducible: `h9_wedderburn_tractability`
probe + the $\dim_q$ and Borromean-action tables above (exact sympy,
braid- and Hecke-relation verified).

### #7 where $\mathfrak{E}_0$ actually lives (corpus-grep result)

The natural follow-up — "if not colour, does the flavour/spatial sector
*derive* $\mathfrak{E}_0$?" — is answered by the corpus, not by new work.
A corpus-grep (`grep -rn 4.155 content/`) finds $\mathfrak{E}_0$ **is
already given a structural $N=0$ value**, in
[`observations/epistemic-status-of-calibrations.md`](../../content/quantum-observable-universe/observations/epistemic-status-of-calibrations.md)
(CAL-3 section) and
[`mass-theory/three-calibration-inputs.md`](../../content/quantum-observable-universe/mass-theory/three-calibration-inputs.md):

$$
\mathfrak{E}_0^{(N=0)} \;=\; \frac{m_e}{q_0\,(q_0-1)} \;=\; 4.18598\ \text{MeV}
\qquad\text{vs}\qquad
\mathfrak{E}_0^{(\text{cal})} = \frac{Q_\beta}{|\Delta(\mathrm{net})|} = 4.15494\ \text{MeV}
\quad(+0.75\%).
$$

So $\mathfrak{E}_0$ is **not** a free 4th parameter and **not** colour: it
is the **electron scale $m_e$ (CAL-1)** times a pure **substrate factor
$1/(q_0(q_0-1))$**. The flavour sector enters the $Q_\beta$ relation only
through $|\Delta(\mathrm{net})|$, the proton$-$neutron *surviving trace
difference* — which, by the #7 result above, is exactly what the $(2,1)$
standard channel carries (the only block whose braid action is
non-scalar). The picture is internally consistent:

| factor in $Q_\beta = |\Delta(\mathrm{net})|\cdot\mathfrak{E}_0$ | sector | status |
|---|---|---|
| $\mathfrak{E}_0 = m_e/(q_0(q_0-1))$ | electron $\times$ substrate | **derived** ($N=0$), $+0.75\%$ |
| $|\Delta(\mathrm{net})|$ | flavour $u$–$d$ typing, $(2,1)$ channel | computed from $H_3$ NF |
| colour $(1^3)$ | confinement | **factor $1$** (#7 above) |

**The genuine open gap is therefore *not* the value of
$\mathfrak{E}_0$** but two upstream items already logged in the corpus
(so neither is newly "open"):

1. the relation $Q_\beta = |\Delta(\mathrm{net})|\cdot\mathfrak{E}_0$ is
   **postulated**, not derived from the canonical per-braid mass formula
   (audit `-q-beta-net-ansatz-fitting-finding.md`);
2. the $+0.75\%$ derived-vs-calibrated gap has **no discriminator** —
   genuine $N=0$ truncation residual vs substrate artefact
   (epistemic-status-of-calibrations.md, CAL-3).

**This session's contribution to #7 is the negative half of that table:**
a rigorous proof that colour resolution contributes a factor of exactly
$1$ (trivial, Borromean, and entangled cases all closed), which *removes
the competing "colour predicts $\mathfrak{E}_0$" hypothesis* and confirms
the existing $m_e/(q_0(q_0-1))$ framing is where the scale lives. No new
derivation of $\mathfrak{E}_0$ is proposed (corpus-grep discipline: it is
already derived at $N=0$; re-deriving it would duplicate
existing content).

**Note:** the bean cites `beta-decay-energy-scale.witness.json`, which
**does not exist** in `folio-assistant/computations/`. The $H_3$
NF₊/NF₋ table in `negative-debt-confinement.md` is not currently backed by
a committed witness; producing one is a prerequisite for any future
$\mathfrak{E}_0$ comparison.

---

## #6 — gram-matrix-h3 determinant: deferral re-confirmed

`gramMatrix_det_eq_factorization`
([`GramMatrixH3Symbolic.lean:364`](../../content/quantum-observable-universe/lean/QOU/Interactions/GramMatrixH3Symbolic.lean))
carries the one `sorry` in the file: the $6\times6$ symbolic determinant
of degree-12 rational functions equals a specific factorization.

A bounded `lean`-direct attempt this session (the documented
`Matrix.det_fin_succ; field_simp; ring` strategy) confirms deferral is
correct:

- `Matrix.det_fin_succ` **does not exist** in Mathlib — a $6\times6$
  determinant needs recursive `Matrix.det_succ_row_zero` (Mathlib only
  ships closed `det_fin_two`/`det_fin_three`);
- even with the correct expansion, the final `ring` faces a
  **degree-$60+$ rational-function identity** (cross-multiplying
  $u^{10}(u^2+1)^{12}$ against every entry denominator) — the
  "expensive rainbow" the formalize-first discipline says to skip;
- the **substantive content is already proved**: the conditional
  discharge `gramMatrix_det_ne_zero_conditional` (6 positivity lemmas +
  denominator positivity ⇒ $\det \ne 0$ for $u > 1$) is sorry-free.

Only the sympy-witnessed factorization identity stays deferred, matching
the file author's "multi-thousand-line work" label. No change.

---

## #4 — bigbang-heatdeath: speculative metaphor, no action

The block is explicitly flagged "highly speculative … metaphor, pending a
separate discussion of cosmological time in QOU." Its **mathematical**
content (QOU functors evaluate at named infinite/infinitesimal surreals;
rational expressions in $q$ make sense at any non-pole element of
$\mathbf{No}$) is already correct. The interpretive content is
deliberately non-committal. Nothing to formalize or compute; no action.
