# Forward derivation — pre-Archimedean algebraic chain
**(categorical action → … → Hecke crossing energy → mass / β-decay / binding)**

**Compiled** 2026-05-02 on `claude/refactor-computation-framework-Dmvva`.
**Predecessors:**
[`2026-05-01-math-framework-deep-audit.md`](2026-05-01-math-framework-deep-audit.md) (line-by-line audit table),
[`derivation-chain-mass-tower.md`](derivation-chain-mass-tower.md) (Lean-side chain),
[`computations/DERIVATION-CHAIN-METHODOLOGY.md`](../../computations/DERIVATION-CHAIN-METHODOLOGY.md) (compute methodology),
[`computations/DERIVATION-STATUS.md`](../../computations/DERIVATION-STATUS.md) (current numerical state).

**What this document is.** A *forward* (rather than retrospective) walk
through the algebraic-side derivation. Each step states (a) the
mathematical content, (b) what it derives from the previous step, (c)
the conjecture(s) it rides on (if any), (d) the compute / Lean backing,
and (e) any **audit flag** for residual fits, guesses, or empirical
inputs. The document is paired with the §1 line-by-line table of the
deep-audit and a refresh of that audit's flags is appended at the end
(§D).

**Strict rules of the game.**

1. **The pre-Archimedean wall** (`prop:three-calibration-discipline`).
   Everything below `τ` (the fibre functor / Archimedean realisation)
   must live in the categorical base ring `R ⊇ ℤ[q,q⁻¹]` or
   `ℚ(q)`. Three external scalar inputs are categorically allowed,
   one per cohomological degree:

   | ID | Calibration | (Co)homology | Role |
   |----|-------------|--------------|------|
   | CAL-0 | $m_e$ (CODATA) | $H^0$ | mass scale |
   | CAL-1 | $m_\mu/m_e$ (CODATA) | $H^1$ | fixes $q_0$ |
   | CAL-2 | $Q_\beta$ (PDG)  | $H^2$ | weak sector |

   Anything else entering as a derivation source is a **wall
   violation** and is flagged 🔴.

2. **Conjectural propagation** (AGENTS.md §3b). Any provable kind
   downstream of a `conj:` block is a `conjecture` itself. Definitions
   may name conjectural objects but do not propagate; they are
   tagged 🟡-axiomatic when their well-formedness rides on a
   `conj:`.

3. **Numerical-only audit flags** are **not** proof gaps. Where the
   only residue is "enumeration time" (e.g. magic number 126 at
   $n=378$), we mark the row 🟡-numerical, not 🟠-fit.

---

## §A. The chain — 19 steps from substrate to Hecke energy

Every step links to its primary `.md` block; siblings (`.lean`,
`.ts`) are listed only when they introduce extra content.

### Step 0 — The substrate

[`def:rigid-monoidal-category`](../../content/quantum-observable-universe/quantum-universes/quantum-universe.md),
[`def:fibre-functor`](../../content/quantum-observable-universe/quantum-observable-universes/quantum-observable-universe.md).

- **Setting.** A rigid monoidal category $\mathbf{C}$ with object
  $A$ and *fibre functor*
  $\tau \colon \mathbf{C} \to R\text{-}\mathrm{Mod}$ where $R$ is a
  commutative ring containing $\mathbb{Z}[q^{\pm 1}]$.
- **Substrate parameter $q$** enters here as the eigenvalue of the
  braiding $c_{V,V}$ on the symmetric summand of $V \otimes V$
  for $V = \tau(A)$.
- **Riding-on:** standard rigid-monoidal axioms (Mathlib
  `CategoryTheory.MonoidalCategory`).
- **Compute backing:** none required at this step.
- **AUDIT.** 🟢 None — clean axiomatic setup.

### Step 1 — Frobenius–Hopf substrate axioms

[`def:frobenius-hopf-substrate`](../../content/quantum-observable-universe/algebraic-substrate/frobenius-hopf-substrate.md)
(+ Lean `frobenius-hopf-substrate.lean`, `substrate-self-duality.lean`).

- **Statement.** $A$ carries a sextuple $(\mu,\eta,\Delta,\varepsilon,
  S)$ with a *Frobenius form* $\lambda\colon A \to \mathbf{1}$
  satisfying associativity, coassociativity, the Hopf compatibility
  $\varepsilon \circ \mu = u\circ(\varepsilon\otimes\varepsilon)$,
  the **Frobenius relation**
  $\mu\circ\Delta = (\Delta\otimes\mathrm{id})\circ\alpha\circ
  (\mathrm{id}\otimes\mu)$, **non-degeneracy**, and **self-duality**
  $A \cong A^\vee$.
- **Derivation from Step 0.** Axiomatic — *defines* what counts as a
  QOU substrate.
- **Riding-on:** Step 0 only. The substrate parameter $q$ enters
  through the *ribbon* / *anti-Yetter–Drinfeld* refinement (see
  Step 6) but is consistent with Step 1 alone.
- **Compute backing:** none — this is the algebraic top of the chain.
- **AUDIT.** 🟢 No fits, no empirical inputs. The Frobenius form
  $\lambda$ is data, not a fit.

### Step 2 — Frobenius pairing and self-duality

[`def:frobenius-pairing`](../../content/quantum-observable-universe/quantum-universes/frobenius-pairing.md),
[`prop:frobenius-pairing-exists`](../../content/quantum-observable-universe/quantum-universes/frobenius-pairing-exists.md),
[`prop:frobenius-pairing-unique`](../../content/quantum-observable-universe/quantum-universes/frobenius-pairing-unique.md).

- **Statement.** $\langle a,b\rangle_F := \lambda(\mu(a\otimes b))$
  is non-degenerate; the induced map $A \to A^\vee$ is iso.
  Existence and uniqueness are 🟡-axiomatic on a generic $\mathbf{C}$;
  for $\mathbf{C} = \mathbf{Rep}(\mathrm{SU}_q(2))$ both are
  proved (Lean: `frobenius-pairing-exists.lean`,
  `frobenius-pairing-unique.lean`, both 0 sorries on the SU(2) variant).
- **Derivation from Step 1.** Direct from the non-degeneracy
  axiom + snake identities.
- **Riding-on:** Step 1.
- **Compute backing:** SU(2) Lean witness only.
- **AUDIT.** 🟢 The general-$\mathbf{C}$ existence/uniqueness
  is honestly 🟡-axiomatic; SU(2) case is 🟢. No empirical input.

### Step 3 — Categorical action $\mathcal{S} = \mathrm{tr}(\Phi)$

[`def:categorical-action`](../../content/quantum-observable-universe/quantum-observable-universes/categorical-action.md),
[`thm:categorical-action-exists`](../../content/quantum-observable-universe/quantum-observable-universes/categorical-action-exists.md),
[`thm:categorical-action-unique`](../../content/quantum-observable-universe/quantum-observable-universes/categorical-action-unique.md).

- **Statement.** A *categorical action* on $(\mathbf{C}, A, \tau)$ is
  a closed loop $\mathcal{S}\colon \mathbf{1}\to\mathbf{1}$ of the
  form
  $\mathcal{S} = \mathrm{ev}_A \circ (\mathrm{id}_{A^\vee}\otimes\Phi)
  \circ\mathrm{coev}_A = \mathrm{tr}(\Phi)$
  for some $\Phi \in \mathrm{End}_{\mathbf{C}}(A)$.
- **Derivation from Step 2.** The pairing identifies $A^\vee \cong A$
  so that $\mathrm{ev}_A$ and $\mathrm{coev}_A$ exist; the closure
  of the loop is forced by rigidity.
- **Riding-on:** existence/uniqueness on generic $\mathbf{C}$ are
  🟡; on SU(2) both 🟢.
- **Compute backing:** Lean `categorical-action.lean` + proofs.
- **AUDIT.** 🟢 No fits. $\Phi$ is the *physics endomorphism*; its
  identification with the Hecke mass element happens at Step 16, not
  here.

### Step 4 — Mass identity

[`def:mass-identity`](../../content/quantum-observable-universe/quantum-observable-universes/mass-identity.md),
[`prop:categorical-mass-markov`](../../content/quantum-observable-universe/braids-and-knots/categorical-mass-markov.md).

- **Statement.** For a vortex $\varrho\colon\mathbf{1}\to A$,
  $$
    \mathfrak{m}(\varrho)
    \;=\;
    \bigl\| \mathrm{tr}\bigl(\,(\textstyle\int_A\!\otimes\,\mathrm{id})
    \circ \Delta \circ \varrho\bigr)\bigr\|_F,
  $$
  the **Frobenius norm** (not Archimedean magnitude) of the trace
  of the integrated comultiplied vortex.
- **Derivation from Steps 1–3.** The integration $\int_A = \lambda$
  is given by the Frobenius form (Step 1); $\Delta$ is coalgebra
  comultiplication; the trace is Step 3 with $\Phi = L_{\alpha}$
  (left-multiplication by the integrand
  $\alpha = (\int_A\otimes\mathrm{id})\circ\Delta\circ\varrho$).
- **Riding-on:** Steps 1–3.
- **Compute backing:** none at this level.
- **AUDIT.** 🟢 No fits. The norm is the **categorical** Frobenius
  norm $\|x\|_F^2 = \langle x, x\rangle_F$, not absolute value;
  *no $\mathbb{R}$ enters yet*.

### Step 5 — Cyclic / Reeb action

[`prop:categorical-reeb-derivation`](../../content/quantum-observable-universe/algebraic-substrate/categorical-reeb-derivation.md).

- **Statement.** When $\mathbf{C}$ is ribbon, the categorical action
  factors through a cyclic / Reeb structure $\mathcal{S}_{\rm Reeb}$
  whose generator is the ribbon twist $\theta_A$.
- **Derivation from Step 3.** Ribbon structure on $\mathbf{C}$
  promotes the closed loop $\mathcal{S}$ to a cyclic-cohomology
  cocycle.
- **Riding-on:** ribbon-structure axiom (part of Step 1's
  refinement to *anti-Yetter–Drinfeld* substrate).
- **Compute backing:** none required here.
- **AUDIT.** 🟢 No fits.

### Step 6 — Non-abelian Stokes / motivic-Galois descent

[`def:motivic-galois-character`](../../content/quantum-observable-universe/lifting-and-descent/motivic-galois-character.md),
[`def:descent-involution`](../../content/quantum-observable-universe/lifting-and-descent/descent-involution.md),
[`conj:motivic-perpetual-obstruction`](../../content/quantum-observable-universe/lifting-and-descent/motivic-perpetual-obstruction.md).

- **Statement.** The motivic-Galois layer of the Yekutieli obstruction
  $\kappa_n \in H^2(\mathcal{S},\mathbb{G}_m)$ is carried by a
  single character
  $\chi^{\mathrm{mot}}_A\colon
  \mathrm{Gal}(\mathbb{Q}(\mu_\infty)/\mathbb{Q})
  \to \mathrm{Aut}_{\widehat{\mathcal{M}}}([A])$.
  The *descent involution* $\hat\tau_n$ on $H_n(q)$ is the
  finite-stage realisation of this character at the cyclotomic
  projection $\rho_p$.
- **Derivation from Steps 4–5.** "Non-abelian Stokes" here means:
  the categorical action $\mathcal{S}$ obstructs non-trivially to
  patch globally on the cosimplicial crossed-groupoid (Step 7);
  the obstruction is exactly $\kappa_n$, and at the motivic level it
  is the single character $\chi^{\mathrm{mot}}_A$.
- **Riding-on:** `conj:motivic-perpetual-obstruction` — non-vanishing
  of $\chi^{\mathrm{mot}}_A$ on the substrate. The class
  `MotivicGaloisCharacter` in the Lean file takes a
  `MotivicSubstrate` instance and exposes $\chi^{\mathrm{mot}}_A$;
  the `sorry` in any concrete instance **is** the substrate axiom,
  not a missing proof (per AGENTS.md §3b).
- **Compute backing:** none at this level — this is the
  pure-substrate layer.
- **AUDIT.** 🟡 *No concrete `instance` of
  `MotivicGaloisCharacter` for the QOU substrate at $q_0$ exists.*
  This is **GAP 6a** of the prior audit and is the principal open
  item on the substrate side. A concrete instance would close the
  motivic-perpetual-obstruction conjecture; until then, the
  algebraic-side mass tower depends on it as an axiom.
- **Cone of falsity (if `conj:motivic-perpetual-obstruction` fails):**
  the Hecke-tower descent (Steps 8–14) loses its motivic
  identification; compute remains valid as a Hecke-algebra
  computation but loses the formal-substrate foundation.

### Step 7 — Cosimplicial crossed-groupoid / global gluing

[`prop:cosimplicial-crossed-groupoid`](../../content/quantum-observable-universe/lifting-and-descent/cosimplicial-crossed-groupoid.md),
[`prop:descent-condition`](../../content/quantum-observable-universe/lifting-and-descent/descent-condition.md),
[`prop:global-gluing`](../../content/quantum-observable-universe/lifting-and-descent/global-gluing.md).

- **Statement.** The cosimplicial crossed-groupoid carries the
  descent data of $\mathcal{S}$; the **descent condition** identifies
  the level-$n$ Čech cocycles compatible with $\hat\tau_n$;
  **global gluing** assembles them into a single global section
  iff the obstruction (Step 6) vanishes.
- **Derivation from Steps 5–6.** Standard cosimplicial-descent
  machinery, applied to the cyclic action with twist $\theta_A$.
- **Riding-on:** Steps 5–6 only.
- **Compute backing:** none at this level.
- **AUDIT.** 🟢 No fits.

### Step 8 — JSJ stratification of $H_n(q)$ (algebraic side)

[`prop:phi-q-tower-jsj-bridge`](../../content/quantum-observable-universe/braids-and-knots/phi-q-tower-jsj-bridge.md)
(algebraic-side §; the *bridge* to geometric JSJ is the conjectural
$\tau$-image identification).

- **Statement (algebraic).** The mass-tower terms partition along
  *filtration depth* in the GS confinement filtration $J^\bullet$:
  - $|S|=0$ (depth 0): descended summand $|\prod_i\hat V_i^{\rm full}|$
    in $J^0/J^1$;
  - $|S|=1$ (depth 1): per-generator $\Phi_q(|\hat V_i^{\rm full}|)$
    in $J^1/J^2$;
  - $|S|=2$ (depth 2): adjacent-pair
    $z^2\Phi_q(|\hat V_i\hat V_j|)$ in $J^2/J^3$
    ([`prop:markov-pair-z2`](../../content/quantum-observable-universe/braids-and-knots/markov-pair-z2.md)).
  This is the **algebraic JSJ** — a stratification entirely in $H_n(q)$,
  $\mathbb{Q}(q)$-rational, with no 3-manifold language.
- **Derivation from Steps 6–7.** Descent involution $\hat\tau_n$
  + GS filtration (Step 13) on the Hecke side. The depth-2 cap
  follows from `markov-pair-z2`: pairs are the largest $|S|$ that
  the Markov property preserves on closure.
- **Riding-on:** Step 6 conjecture; Step 13 GS filtration.
- **Compute backing:**
  [`computations/sdp_cross_channel.py`](../../computations/sdp_cross_channel.py)
  implements the depth-2 cross-pair contribution (level-3 only —
  audit gap §3·D).
- **AUDIT.** 🟢 (post-PR #500) — the algebraic JSJ now lives entirely
  in $J^\bullet$-stratification language. The conjectural piece
  `conj:phi-q-tower-jsj-bridge` is the **bridge** to the geometric
  JSJ via $\tau_{\rm arch}$; its falsity does not invalidate the
  algebraic stratification.

### Step 9 — Chern–Simons / Jones–Wenzl idempotents

[`def:hecke-normal-form`](../../content/quantum-observable-universe/braids-and-knots/skein-generation.md)
(Hecke–Skein dictionary §7a of AGENTS.md),
[`prop:wedderburn-mass-formula`](../../content/quantum-observable-universe/braids-and-knots/wedderburn-mass-formula.md),
[`prop:markov-pair-z2`](../../content/quantum-observable-universe/braids-and-knots/markov-pair-z2.md).

- **Statement.** The Jones–Wenzl idempotents $p_\lambda \in H_n(q)$
  project onto the Wedderburn block of partition $\lambda \vdash n$;
  the Hecke generator $\sigma_i$ has eigenvalues $(q,-q^{-1})$
  on $S^2/\Lambda^2$ giving the Hecke relation
  $(\sigma_i-q)(\sigma_i+q^{-1}) = 0$.
- **Derivation from Steps 1, 6.** $R$-matrix from the substrate's
  ribbon structure; the JW idempotents are the canonical block
  projectors of the Hecke quotient of the braid-group algebra.
- **Riding-on:** Steps 1, 6.
- **Compute backing:**
  [`hecke_core.py`](../../computations/substrate/hecke_core.py)
  (H₃(q) NF multiplication),
  [`hecke_characters.py`](../../computations/hecke/hecke_characters.py)
  (Hoefsmit seminormal matrices, k≤12+).
- **AUDIT.** 🟢 The CS-side / TQFT path-integral interpretation
  lives at $\tau$ and is not used as a derivation input on the
  algebraic side. The Hecke–Skein dictionary is a textbook
  identity (Kassel, Jones).

### Step 10 — Wedderburn–Artin block decomposition

[`prop:wedderburn-mass-formula`](../../content/quantum-observable-universe/braids-and-knots/wedderburn-mass-formula.md),
[`prop:wedderburn-bratteli-recursion`](../../content/quantum-observable-universe/braids-and-knots/wedderburn-bratteli-recursion.md),
[`prop:three-parameters-wedderburn`](../../content/quantum-observable-universe/braids-and-knots/three-parameters-wedderburn.md).

- **Statement.**
  $H_n(R, q) \cong \bigoplus_{\lambda\vdash n} M_{f_\lambda}(R)$,
  where $f_\lambda$ is the dimension of the Specht module $S^\lambda$.
  At $n = 3$: three blocks (sym + std + alt), giving the
  three-invariant mass formula
  $\mathfrak{m} = Z\,m_{\mathfrak p} + N\,m_{\mathfrak n} + Z\,m_e
  + \alpha(\Phi_1 - 2[3]_q\,\Phi_2 + H_A^2\,\Phi_3)$.
- **Derivation from Step 9.** Wedderburn–Artin applied to the Hecke
  quotient at generic $q$; the Bratteli recursion gives the
  inductive decomposition $H_{n+1}(q) = \mathrm{Ind}^{H_{n+1}}_{H_n}
  H_n(q)$.
- **Riding-on:** Step 9.
- **Compute backing:**
  [`atom-mass-complete-wedderburn.witness.json`](../../computations/atom-mass-complete-wedderburn.witness.json),
  [`atom_mass_partition.py`](../../computations/atom_mass_partition.py).
- **AUDIT.** 🟡 *Bratteli recursion at higher levels* — the
  Lean file `wedderburn-bratteli-recursion.lean` had 2 sorries at
  the time of the 2026-05-01 audit; **post-PR #500** these are
  bounded by the `BringShellBinding` framework and the n=2
  algebraic-primality reduction (commit `0ddcf892`). The recursion
  is closed in narrative; sorries remain at the Lean level.

### Step 11 — Schur–Weyl / Hoefsmit seminormal form

[`prop:hoefsmit-scattering-pipeline`](../../content/quantum-observable-universe/braids-and-knots/hoefsmit-scattering-pipeline.md),
[`prop:hoefsmit-seminormal-form`](../../content/quantum-observable-universe/braids-and-knots/hoefsmit-seminormal-form.md),
[`prop:explicit-alpha-k-h3`](../../content/quantum-observable-universe/braids-and-knots/explicit-alpha-k-h3.md).

- **Statement.** Schur–Weyl: $H_n(q) \cong
  \mathrm{End}_{U_q\mathfrak{sl}_2}(V^{\otimes n})$. Hoefsmit
  seminormal form: $T_i$ acts on the standard tableau basis via
  $a_\rho = h/(1-q^{-2\rho})$ where $\rho$ is the axial distance
  between $i, i+1$ in the tableau.
- **Derivation from Step 10.** Hecke relation
  $\sigma_i^2 = h\,\sigma_i + 1$ + $\det\sigma_i = -1$ + the
  fact that $T_i$ permutes axial distances by 1.
- **Riding-on:** Step 10.
- **Compute backing:**
  [`hoefsmit_witness.json`](../../computations/hoefsmit_witness.json)
  (191→1000+ partitions),
  [`hoefsmit_witness.py`](../../computations/hoefsmit_witness.py).
- **AUDIT.** 🟢 Derived (compute backbone). No fits.

### Step 12 — Partition weights as Wedderburn-block index

[`prop:wedderburn-weight-canonical`](../../content/quantum-observable-universe/braids-and-knots/wedderburn-weight-canonical.md),
[`prop:y-lambda-recipe-from-partition`](../../content/quantum-observable-universe/braids-and-knots/y-lambda-recipe-from-partition.md).

- **Statement.** The Markov trace decomposes as
  $\mathrm{tr}_M = \sum_\lambda y_\lambda\,\chi^\lambda$
  where $y_\lambda$ is the **Jones–Markov central coefficient**
  ($y_\lambda \in \mathbb{Z}[q^{\pm 1}]$ via the Wenzl bridge), and
  $\chi^\lambda$ is the irreducible character. The weight
  $y_\lambda$ has a closed form via cyclotomic factorisation (≤ n=12).
- **Derivation from Steps 10–11.** Linearity of the trace + the
  Hoefsmit-NF expansion of $\rho_\lambda$.
- **Riding-on:** Steps 10–11.
- **Compute backing:**
  [`y_lambda_wenzl_bridge_extended.py`](../../computations/y_lambda_wenzl_bridge_extended.py),
  [`y-lambda-clean-closed-forms.md`](../../computations/y-lambda-clean-closed-forms.md).
- **AUDIT.** 🟢 Derived. The previous "approx" tag on $y_{(4,1)} +
  y_{(2,1,1,1)}$ (BW-11) is **resolved** — closed form available
  at $n \leq 12$.
- **Notation collision warning** (AGENTS.md §7aa): $y_\lambda$ here
  is the Jones–Markov central coefficient (sign-indefinite at
  $n\geq 4$); do **not** confuse with $u_\lambda$ (LP shadow
  price, non-negative by LP duality, used at Step 19). The two
  have collided in older drafts.

### Step 13 — Gröbner–Shirshov filtration $J^\bullet$

[`prop:gb-spectral-sequence`](../../content/quantum-observable-universe/braids-and-knots/gb-spectral-sequence.md),
[`prop:graded-trace-residue-split`](../../content/quantum-observable-universe/braids-and-knots/graded-trace-residue-split.md),
[`prop:confinement-level-exists`](../../content/quantum-observable-universe/braids-and-knots/confinement-level-exists.md).

- **Statement.** The confinement filtration $J^\bullet(q)$ on
  $H_n(R, q)$ is induced by the three GS rewriting rules
  ($d_H$ Hecke, $d_F$ far-commutativity, $d_{YB}$ Yang–Baxter).
  Setting $d = d_H + d_F + d_{YB}$ gives a **filtered Hochschild
  cochain complex** $C^\bullet(H_n(R,q))$ with $d\circ d = 0$
  (Cartan–Eilenberg 1956), and a **GB spectral sequence**
  $E_r^{\ell, *}$ with $E_\infty \Rightarrow \mathrm{gr}\,H_n(R,q)$.
- **Derivation from Step 9.** GS rewriting on the braid-Hecke ideal;
  Hochschild $d\circ d = 0$ is classical; convergence is bounded
  + exhaustive + finite-dimensional at each degree (Weibel §5.5).
- **Riding-on:** Step 9 + the **finite-collapse-at-$E_2$ axiom**
  (`gradedMarkovTrace` and `residueAtRoot` are
  `noncomputable opaque` per
  [`AUDIT-gb-residue-opaque-declarations.md`](../../computations/AUDIT-gb-residue-opaque-declarations.md)).
- **Compute backing:** symbolic-in-$q$ machinery in
  [`hecke_characters.py`](../../computations/hecke/hecke_characters.py)
  (sparse, k≤12+).
- **AUDIT.** 🟡 The *spectral-sequence existence* is now derived
  via the standard Hochschild route (post-update to
  `gb-spectral-sequence.md`). The *term-by-term identification*
  of $E_\infty^{\ell, *}$ with the six mass-formula pieces remains
  a research-level computational task. **Six declarations remain
  `noncomputable opaque`** in the Lean side (`gradedMarkovTrace`,
  `residueAtRoot`, `spectral_decomposition`, `spectral_sum_finite`,
  two `archimedean_agreement`); these are the principal **GAP 13a**.

### Step 14 — DB filtration / direct-limit algebra

[`def:brane-tower-levels`](../../content/quantum-observable-universe/lifting-and-descent/brane-tower-levels.md),
[`def:direct-limit-algebra`](../../content/quantum-observable-universe/lifting-and-descent/direct-limit-algebra.md).

- **Statement.** The DB (descent–Bratteli) filtration is
  $A_{n+1} = A_n \otimes \Omega^1(A_n)$; the direct-limit algebra
  $A_\infty = \mathrm{colim}\,A_n$ exists by cofinality.
- **Derivation from Steps 7, 13.** Bratteli recursion (Step 10
  inductive structure) + descent involution (Step 7) + GS
  filtration (Step 13) on each $A_n$.
- **Riding-on:** Steps 7, 13.
- **Compute backing:** none required at this level.
- **AUDIT.** 🟡 Uniform $\Delta_{\max}$ bound on per-level descent
  residue is **GAP 14a** of the prior audit. PR #500's
  `cohomology probe` (commit `68351d78`) and `BB-stratification`
  (commit `cffbf553`) bound the residue per stratum but do *not*
  produce a uniform-in-$n$ bound. Open.

### Step 15 — Categorical jet prolongation

[`prop:categorical-jet-prolongation`](../../content/quantum-observable-universe/lifting-and-descent/categorical-jet-prolongation.md),
[`prop:jet-prolongation-C`](../../content/quantum-observable-universe/lifting-and-descent/jet-prolongation-C.md).

- **Statement.** $J^1(A)$ inherits a Frobenius–Hopf structure from
  $A$, so $(\mathbf{C}, J^1(A), \tau')$ is again a quantum universe.
- **Derivation from Steps 1, 5.** A categorical connection
  $\nabla$ (which exists for ribbon $\mathbf{C}$) lifts the
  substrate to the jet bundle; the Frobenius structure pulls back.
- **Riding-on:** Steps 1, 5.
- **Compute backing:** none required.
- **AUDIT.** 🟢 Derived. No fits.

### Step 16 — Markov trace $\mathrm{tr}_M$

[`thm:jones-markov-trace`](../../content/quantum-observable-universe/braids-and-knots/jones-markov-trace.md),
[`prop:markov-trace-frobenius-selection`](../../content/quantum-observable-universe/braids-and-knots/markov-trace-frobenius-selection.md).

- **Statement.** A unique linear functional
  $\mathrm{tr}_M\colon H_n(q) \to \mathbb{Z}[q^{\pm 1}]$ exists
  satisfying cyclicity, normalisation $\mathrm{tr}_M(1) = 1$, and the
  *Markov property* $\mathrm{tr}_M(\sigma_n\,x) = z\,\mathrm{tr}_M(x)$
  for $x \in H_n(q)$ where $z = 1/(q^{1/2} + q^{-1/2})$.
- **Derivation from Steps 10–12.** Weighted sum
  $\mathrm{tr}_M = \sum_\lambda y_\lambda\,\chi^\lambda$ with the
  $y_\lambda$ pinned by Markov + cyclicity (Jones–Ocneanu–Wenzl).
- **Riding-on:** Steps 10–12.
- **Compute backing:**
  [`hecke_core.py`](../../computations/substrate/hecke_core.py)
  Markov trace,
  [`hoefsmit_witness.json`](../../computations/hoefsmit_witness.json).
- **AUDIT.** 🟢 Classical theorem; no fits.

### Step 17 — All-pairs theorem for jet-tower mass

[`prop:markov-pair-z2`](../../content/quantum-observable-universe/braids-and-knots/markov-pair-z2.md),
[`thm:markov-trace-factorization`](../../content/quantum-observable-universe/braids-and-knots/markov-trace-product.md).

- **Statement.** Trace factorisation:
  $\mathrm{tr}_M(\sigma_i\sigma_j) = z^2$ for adjacent $|i-j|=1$.
  This is the **depth-2 cap** — pairs (not triples) are the largest
  $|S|$ at which the Markov property preserves closure.
- **Derivation from Step 16.** Two applications of the Markov
  property.
- **Riding-on:** Step 16.
- **Compute backing:**
  [`pentagon-trace-vs-operator.md`](2026-05-02-r7-pentagon-trace-vs-operator.md)
  + adjacent-vs-full probe.
- **AUDIT.** 🟡 The **pentagon $uv = q\,vu$ verification** at the
  traced-volume level remains GAP 17a (line 113 of the
  2026-04-20 audit); **descent sharpness on pairs** remains
  GAP 17b (line 114). Both are residual, not load-bearing.

### Step 18 — Mass endomorphism tower

[`prop:mass-endomorphism-tower`](../../content/quantum-observable-universe/braids-and-knots/mass-endomorphism-tower.md),
[`def:hecke-mass-element`](../../content/quantum-observable-universe/braids-and-knots/hecke-mass-element.md),
[`conj:mass-endomorphism`](../../content/quantum-observable-universe/braids-and-knots/mass-endomorphism-tower.md).

- **Statement.** The mass endomorphism is
  $\Phi_{\rm mass}(\beta) = \tau(L_{\alpha_\varrho}) \in H_n(q)$
  where $\alpha_\varrho = (\int_A\otimes\mathrm{id})\circ\Delta\circ\varrho$
  and $L_\alpha$ is left-multiplication. The descent splitting
  $\Phi_{\rm mass} = \Phi^{\rm desc} + \Phi^{\rm trans}$ with
  $\Phi^{\rm desc} = \tau(\hat\tau_n(L_\alpha))$ encodes the
  base-level cycle.
- **Derivation from Steps 4, 6, 16.** $\alpha_\varrho$ comes from
  Step 4; the descent involution $\hat\tau_n$ from Step 6; the
  embedding $\tau\colon \mathrm{End}_\mathbf{C}(A) \hookrightarrow
  H_n(q)$ via Schur–Weyl (Step 11) sends $L_\alpha$ to the Hecke
  element.
- **Riding-on:** Steps 4, 6 (motivic descent), 11, 16.
- **Compute backing:**
  [`mass-formula-wedderburn-enumeration.lean`](../../content/quantum-observable-universe/braids-and-knots/mass-formula-wedderburn-enumeration.lean),
  [`crt_markov.py`](../../computations/crt_markov.py)
  (the CRT engine).
- **AUDIT.** 🟡 `conj:mass-endomorphism` claims the tower is a
  *single closed-form* $H_n(q)$ element. As of PR #500 the
  conjecture is open at *closed-form* level; the tower remains
  correct as an infinite series. `crt_markov.py` is **std-channel
  + descended-only** (audit §3·A: ~99% of mass missing!) — this is
  the **single largest compute fix** still open.

### Step 19 — Hecke crossing energy

[`def:crossing-energy`](../../content/quantum-observable-universe/braids-and-knots/crossing-energy.md)
(Lean: 0 sorries),
[`prop:hecke-mass-trace`](../../content/quantum-observable-universe/braids-and-knots/hecke-mass-trace.md).

- **Statement.**
  $\mathfrak{E}_{\rm cross}(\mathfrak{H}) = |\mathrm{tr}_M(\Phi_{\rm mass})|$
  where $|\cdot|$ is the **Frobenius norm** in
  $\mathbb{Z}[q^{\pm 1}]$ (not Archimedean). Per-crossing weights
  $(q, -q^{-1})$ are the **two eigenvalues of the Hecke generator**
  $T = P\circ R$ (not external postulates) — forced by rigidity +
  $\det(R) = 1$ + $P|_{\Lambda^2 V} = -\mathrm{id}$.
- **Derivation from Steps 16, 18.** Markov trace (Step 16) of the
  mass element (Step 18); the eigenvalue forcing comes from
  Step 9.
- **Riding-on:** Steps 9, 16, 18.
- **Compute backing:** Lean `crossing-energy.lean` (0 sorries);
  Python via `hecke_core.py`.
- **AUDIT.** 🟢 Lean-clean. The per-crossing weights are
  *categorically forced*, not fitted.

---

## §B. From Hecke energy to physics — the "applied" layer

Steps 1–19 stay strictly pre-Archimedean. The **physics outputs**
(masses, Q-values, binding energies, fine-structure constant) require
*one* application of the fibre functor $\tau$ (mass scale via
$m_e$ at CAL-0) and at most three external scalar inputs (CAL-0/1/2).
Below: how each output sector consumes the chain.

### B.1 — Mass-tower output

- **Recipe.** For an atom $(Z, N)$:
  1. Form atomic braid $\mathcal{A} \in H_{A+Z}(q)$.
  2. Compute $\Phi_{\rm mass}(\mathcal{A})$ via Step 18.
  3. Apply Markov trace (Step 16) → element of $\mathbb{Z}[q^{\pm 1}]$.
  4. Substitute $q = q_0$ at the **final** step.
  5. Multiply by $m_e$ (CAL-0).
- **Audit.** §3·E of prior audit: the proton/neutron/atom paths
  currently substitute $q_0$ **early**, not at the final step. This
  is the largest source of "fitted-feeling" numbers in the witness
  JSONs; **not a math-framework gap** but a **compute hygiene gap**.
  Symbolic-in-$q$ throughout is workplan item P3 (Track A).
- **Numerical state (DERIVATION-STATUS.md):** k=5 mass MAE 0.006%
  on 45 isotopes. Convergence pattern MAE(k) ≤ 0.035%·[2]²⁻⁽ᵏ⁻³⁾.

### B.2 — Beta-decay sector (CAL-2 = $Q_\beta$)

- **Recipe.** Q-value Q(parent → daughter) = m(parent) − m(daughter)
  − {electron / neutrino mass corrections}, all computed via the
  same Hecke-mass pipeline (B.1). The $H^2$ calibration enters as
  $E_0 = Q_\beta(\mathrm{n}\to\mathrm{p}) = 0.782$ MeV — a **single
  scalar** that fixes the weak-sector normalisation, *not* a
  per-isotope fit.
- **Numerical state (sector audit, 2026-05-02).** Q-values are
  largely categorical: Q(n→p) = 0.7816 vs 0.78233 MeV (-0.1%);
  Q(³H→³He) = 18.23 vs 18.59 keV (-2%); ⁶⁰Co, ¹³⁷Cs,
  ²¹⁰Bi predicted within categorical degree-2 + magic-shell
  Pauli corrections (no fitting). MAE 0.006% over 45 isotopes at
  k=5.
- **🔴 NV-1 — NEW HARD FLAG.** The *Fermi constant* decomposition
  $G_F = 1/(\sqrt 2\,v^2)$ with $v = N_v\,E_\times\,\mu_0$
  treats $N_v \approx 1.45\times 10^6$ (the **effective weak-scale
  crossing count**) as a topological invariant of the
  brane-tower. **In the current code path
  ([`beta-decay-from-q.py`](../../computations/beta-decay-from-q.py)
  lines 104–108) $N_v$ is read backward from the CODATA value of
  $v$ — not derived.** The script explicitly flags this as
  "OPEN COMPUTATION". This is the **single largest blocker** for
  fully-categorical β-decay rates. Half-lives scale as
  $G_F^2 \propto N_v^{-4}$, so a derivation of $N_v$ would close
  every β-decay rate prediction. **Status: open research.**
- **🔴 FROB-FILTER — NEW FLAG.** The
  *Frobenius-positivity filter* used in
  [`branching-qvalues.witness.json`](../../computations/branching-qvalues.witness.json)
  switches between $\|\Sigma_{\rm all}\|$ (A=3 case) and
  $\|\Sigma_{\rm FP}\|$ (A=6 case). The activation threshold is
  **not categorically justified**; the witness explicitly lists
  it as "open problem: Frobenius filter activation threshold
  between A=3 and A=6 needs derivation." Likely this is a
  threshold on LP-dual eigenvalues (per `prop:mass-coefficient-shadow-price`),
  but the current rule is empirical.
- **🟡 Φ_q truncation (residual).** The 2% gap on Q(³H→³He)
  closes on switching from truncated series (max_iter=2000) to
  exact Habiro cyclotomic form. Not a fit, just a numerical
  upgrade.
- **Verdict (sector).** β-decay sector is ~85% categorically
  derived: Q-values, shell corrections, degree-2 suppression,
  Pauli magic effects all derive from $(q_0, m_e)$ + CAL-2.
  Residual 15% rides on (i) NV-1, (ii) FROB-FILTER threshold,
  (iii) Φ_q series order, (iv) full triple-loop tower implementation
  (compute §3·A).

### B.3 — Binding-energy / BW formula

- **Recipe.** The 11 BW terms at k=5 are 11 q-integer coefficients
  derived from Wedderburn block dimensions (Step 10) + Hoefsmit
  branching (Step 11) + scaling functions in $(Z, N, A)$. Each
  term has the form $C_\lambda \cdot S_\lambda(Z, N, A) \cdot m_e$
  with $C_\lambda \in \mathbb{Z}[q_0^{\pm 1}]$ and $S_\lambda$
  rational in $A^{1/3}$.
- **Branching to k=6.** `prop:mass-coefficient-shadow-price` — each
  BW coefficient is the **LP shadow price** of the partition's
  Frobenius positivity constraint in the nuclear operator-selection
  LP. The branching rule
  $C_\mu = \sum_{\lambda \nearrow \mu}
  [\dim_q(\mu)/\sum_{\mu':\lambda\nearrow\mu'}\dim_q(\mu')]\,C_\lambda$
  propagates known coefficients without fitting.
- **Sector audit (2026-05-02) — coefficients.** 10 of 11 coefficients
  are 🟢 *fully derived*: q-hook products (BW-8 Hook), Wenzl-bridge
  partitions (BW-11 pn-corr), Wedderburn-block weights (Volume,
  Surface, Coulomb, Asymmetry, Pairing, Exchange, Wigner, Form
  factor). No fits.
- **🟡 Term 7 (Shell) scaling function — REFINED FLAG.** Prior audit
  treated only the *magic ladder identification* as conjectural.
  The sector audit clarifies that the **scaling form
  $f_{\rm magic}/A^{2/3}$ itself depends on
  `conj:homological-shell-condensation`** — i.e. the BW Term 7
  scaling function is *conjectural*, not just empirically
  validated. The **coefficient** $[2]_q^2 [3]_q\,m_e$ is
  derived from [3,1] Wedderburn blocks (🟢); the **functional
  form** of the scaling rides on the conjecture (🟡).
- **🟡 LP cost vector seeding.** The k=6 branching LP itself is
  categorical (Frobenius reciprocity, Bratteli diagram). But the
  **cost vector** uses the magic-shell ladder via
  [`qvalue-unified.py`](../../computations/qvalue-unified.py)'s
  `lp_shadow_price(Z, N)` function, which depends on magic-shell
  membership — that is, on `conj:homological-shell-condensation`.
  No AME mass data feeds the LP directly (no least-squares on
  masses), but the magic-ladder structure is the linchpin.
- **🟠 Compute hygiene §3·E status.**
  [`hecke_core.py`](../../computations/substrate/hecke_core.py)
  three-term formula (Volume / Coulomb / chirality) **still
  substitutes $q_0$ early into $[3]_q$, $H_A$** (lines 49–52).
  [`exact_binding_per_operation.py`](../../computations/exact_binding_per_operation.py)
  maintains symbolic-in-$q$ at 100-dip mpmath precision; partition
  paths via Wenzl-bridge are fully symbolic. The early-q₀
  substitution in `hecke_core.py` is **the principal compute
  hygiene gap**, not a math-framework gap.
- **Verdict (sector).** Coefficients clean, scaling functions
  10/11 categorical + 1/11 conjectural-form (Term 7). LP at k=6
  categorical-in-form, conjecture-seeded-in-cost-vector. Compute
  hygiene improving but not complete. MAE 0.006% on 45 isotopes
  at k=5 within derivation budget.

### B.4 — Fine-structure $1/\alpha_{\rm EM}$

- **Recipe.** $1/\alpha_{\rm EM} = 45\,[3]_q\,(1 + \delta_{CS}
  + 8q\,\delta_{CS}^2)$ with $\delta_{CS} = \hbar_q^4\,[5]_q$.
  Each factor traces upstream: $45 = \binom{10}{2}$ via
  exterior-square Borromean (Step 12); $[3]_q$ via the substrate
  parameter (CAL-1); $\delta_{CS}$ via genus-4 torus-knot
  enumeration (Step 9 / 18); the $8q\,\delta_{CS}^2$ correction
  via gram-determinant Plancherel ratio.
- **Audit.** Prior §2·E: 6.7 ppb residual — **within CODATA
  21-ppb uncertainty**. PSLQ uniqueness witness rules out shorter
  rational combinations. **Closed.**

---

## §C. Where new content has to land — what's missing on the algebraic side

Cross-referenced against §A audit flags and current branch state
(post-PR #500 algebraic refactor merged 2026-05-02):

### C.1 — Substrate-side gaps

| ID | Gap | Step | Impact if open | Action |
|----|-----|------|----------------|--------|
| **6a** | No concrete `instance` of `MotivicGaloisCharacter` for QOU substrate at $q_0$ | 6 | Substrate axiom; compute unaffected | research-grade — track on `family-4-motivic-path.md` |
| **13a** | Six `noncomputable opaque` declarations on the GS side (`gradedMarkovTrace`, `residueAtRoot`, `spectral_decomposition`, `spectral_sum_finite`, two `archimedean_agreement`) | 13 | Empirical witness substitutes; narrative needs explicit conjecture statement | author conjectures with explicit GS dependencies |
| **14a** | Uniform $\Delta_{\max}$ bound on per-level descent residue | 14 | Per-stratum bounds exist; uniform-in-$n$ does not | open research |
| **17a** | Pentagon $uv = q\,vu$ at traced-volume level | 17 | Sharpness check; not load-bearing | residual |
| **17b** | Descent sharpness on pairs | 17 | Same as 17a | residual |
| **18a** | `conj:mass-endomorphism` closed form | 18 | Tower remains correct as series | research-grade |

### C.2 — Compute-side gaps

| ID | Gap | Step | Impact | Action |
|----|-----|------|--------|--------|
| **3·A** | `crt_markov.py` is std-channel only, descended-only | 18 | ~99% of mass tower missing | **single largest compute fix** |
| **3·B** | Wedderburn coverage at $H_{3A}(q)$ uses $H_3$ weights | 10 | Approximation at $A \geq 4$ | CRT polynomial reconstruction |
| **3·C** | Word-shortcut undo functions for levels 4–7 | — | $A \geq 12$ ground-truth missing | infrastructure |
| **3·D** | Multi-level quadratic SDP only at level 3 | 8 | Levels 4–7 cross-terms missing | infrastructure |
| **3·E** | Symbolic-in-$q$ throughout; $q_0$-substitution at final step | B.1 | "Fitted-feeling" numbers in witnesses | hygiene |
| **3·F** | GB-residue opaque axioms | 13 | Same as 13a above | conjecture-author |

### C.3 — Mathematical-statement gaps (numerical-only or framework)

| ID | Gap | Sector | Action |
|----|-----|--------|--------|
| **MAG-126** | Magic number $Z=126$ at $n=378$ | Magic ladder | Cron compute (~10⁷ partitions); not a proof gap |
| **conj:homological-shell-condensation** | "BB collapse → magic ladder" (not just $\kappa = 0$) | Step 12 / Step 8 / BW Term 7 scaling | Open; affects shell-correction scaling form |
| **conj:phi-q-tower-jsj-bridge** | Algebraic JSJ ↔ geometric JSJ under $\tau_{\rm arch}$ | Step 8 | $\tau$-image bridge; algebraic side unaffected |

### C.4 — β-decay sector gaps (NEW from 2026-05-02 audit)

| ID | Gap | Sector | Action |
|----|-----|--------|--------|
| **🔴 NV-1** | Effective weak-scale crossing count $N_v\approx 1.45\times 10^6$ read backward from CODATA, not derived from brane-tower topology | β-decay rates / $G_F$ | **Single largest blocker for categorical β-decay rates.** Needs identification of $N_v$ as a topological invariant (likely a count of crossings in the EW sub-tower). Half-lives scale as $G_F^2 \propto N_v^{-4}$. |
| **🔴 FROB-FILTER** | Frobenius-positivity filter activation threshold A=3 → A=6 not categorically justified | β-decay Q-values for A≥6 | Likely a threshold on LP-dual eigenvalues per `prop:mass-coefficient-shadow-price`; needs derivation. |
| **🟠 GT-MATRIX** | Gamow-Teller matrix element $g_A = 1.275$ stated as target but **not yet computed** from Borromean Skein-algebra trace | β-decay rates | "Open computation" in `beta-decay-from-q.py` — research-grade. |
| **🟡 Φ_q-TRUNC** | Φ_q series truncated at max_iter=2000; 2% gap on Q(³H→³He) | Q-value precision | Replace by exact Habiro cyclotomic form. Numerical, not proof gap. |

### C.5 — Binding-energy sector gaps (refined 2026-05-02)

| ID | Gap | Sector | Action |
|----|-----|--------|--------|
| **🟡 SHELL-7-SCALE** | BW Term 7 scaling form $f_{\rm magic}/A^{2/3}$ is *conjectural*, depending on `conj:homological-shell-condensation` (refined from prior "magic-ladder identification only") | BW formula | Closing requires either proof of the conjecture or alternative derivation of the scaling form |
| **🟡 LP-COST-MAG** | k=6 LP cost vector seeded from magic-shell structure (so depends on `conj:homological-shell-condensation`); no AME mass data fed directly | k=5→k=6 branching | Same closure as SHELL-7-SCALE |
| **🟠 HECKE-EARLY-Q0** | `hecke_core.py` three-term formula substitutes $q_0$ early into $[3]_q$, $H_A$ (lines 49–52) | Compute hygiene | §3·E migration to ℤ[q^{±1}] throughout; tracked on `2026-05-02-p2-5-symbolic-in-q-migration.md` |

---

## §D. Audit-flag refresh against `2026-05-01-math-framework-deep-audit.md`

The 2026-05-01 audit's §6 scorecard reported:

> 14/19 🟢 proved, 4/19 🟡 conjectural, 0/19 🔴 wall-violation,
> 0 hard empirical flags + 1 numerical-only (MAG-1).

**Post-PR #500 + post-merge state (2026-05-02):**

| Item | 2026-05-01 status | 2026-05-02 status | Change |
|------|-------------------|-------------------|--------|
| Step 6 (motivic) | 🟡 conjectural — `family-4-motivic-path` | 🟡 unchanged | — |
| Step 8 (JSJ) | 🟢 algebraic recast (P0.3) | 🟢 unchanged + reinforced via PR #500 BringShellBinding | improved |
| Step 10 (Wedderburn–Bratteli) | 🟡 2 sorries | 🟡 narrative-closed via BringShellBinding; Lean sorries remain | improved |
| Step 13 (GS filtration) | 🟡 6 opaque axioms | 🟡 spectral-sequence existence now derived via Hochschild route; 6 opaques remain | improved |
| Step 14 (DB filtration) | 🟡 GAP 14a | 🟡 PR #500 cohomology-probe + BB-stratification bound per-stratum; uniform-in-$n$ open | partial |
| Step 17 (pentagon) | 🟡 GAP 17a/b | 🟡 unchanged | — |
| Step 18 (mass endo) | 🟡 GAP 18a | 🟡 unchanged | — |
| MAG-1 | 🟢 6/7 derived, 1/7 enumeration | 🟢 unchanged + framework reinforced via PR #500 6-knot combinatorial basis | improved |
| ALPHA-2 | 🟢 6.7 ppb (closed) | 🟢 unchanged | — |
| BW-8, BW-11 | 🟢 Wenzl-bridge closed | 🟢 unchanged | — |
| CAL-0/1/2 | 🟢 declared | 🟢 unchanged | — |

**Net change post-PR #500.** No new wall violations introduced; no
new fits; the major framework additions (BringShellBinding, BB
spectral-sequence, MagicLadderEquivalences) **deepen** the algebraic
side without crossing the wall. The audit headline is **unchanged**:
14/19 clean, 5/19 honestly conjectural (`conj:` blocks), 0/19
violations.

The **biggest open lever** for closing the audit is still §3·A
(`crt_markov.py` covering all Wedderburn channels and the full
$\Phi_q$ tower) — closing it would convert the ~99% missing mass
into a **derived** quantity rather than the current "descended-only"
truncation. This is **compute work, not math-framework work**.

---

## §E. New content to watch on `main`

PR #500 (commits `7db4af1b..0fb566da`) is now merged. The next
landings to integrate:

1. **`pl-jsj-mass-integration-equivalence.md`** on
   `claude/quantum-dilogarithm-implementation-DJmlU` — when it
   lands on main, apply the same algebraic-JSJ recast as
   `phi-q-tower-jsj-bridge.md` (P0.3 closure pattern).
2. **`y-lambda-clean-closed-forms.md`** extension to $n > 12$ —
   would close the "Wenzl-bridge $n \leq 12$" qualifier on Step 12.
3. **`crt_markov.py` full-channel coverage** — the §3·A fix.
4. **Symbolic-in-$q$ migration** of the proton/neutron/atom paths
   — the §3·E fix; tracked on
   [`2026-05-02-p2-5-symbolic-in-q-migration.md`](2026-05-02-p2-5-symbolic-in-q-migration.md).

---

**End of forward-derivation document.** This document is paired
with the line-by-line audit in
[`2026-05-01-math-framework-deep-audit.md`](2026-05-01-math-framework-deep-audit.md);
together they cover (forward) "how every algebraic-side claim is
derived" and (backward) "where every numerical input enters". The
three sector audits (mass / β-decay / binding) are produced as
separate parallel reports and will be cross-linked here when they
land.

---

## §F. 2026-05-03 audit refresh

The pre-Archimedean proof + Lean audit
[`2026-05-03-pre-archimedean-proof-audit.md`](2026-05-03-pre-archimedean-proof-audit.md)
re-audits Steps 0–19 cluster-by-cluster against this forward
derivation, fixes the Lean-encoding gaps it finds, and promotes
the cluster modules into the formal Lake package.  The aggregate
result is a substantial reduction in residual gaps:

### Updated GAP scoreboard

| Gap | 2026-05-02 status | 2026-05-03 status (post-audit) | Mechanism |
|-----|-------------------|--------------------------------|-----------|
| §1 wall breaches (17 Lean files) | n/a (introduced by this audit) | **0** (16 fixed; 1 reclassified as Archimedean-by-design) | §1 |
| **6a** — motivic conjecture | 🟡 | 🟡 (formal-chain conditional class ready; instance still open math) | §8 |
| **8** — Φq–JSJ bridge | 🟡 | 🟢 algebraic-stratification side / 🟡 bridge by design (formal Lean, no `sorry`) | §7 + F4 follow-up |
| **13a** — GS-residue opaques (six declarations) | 🟡 | **🟢 0 opaques remain in cluster's `prop:` blocks**; conjectural inputs concentrated in named class fields | §9 |
| **14a** — uniform Δ_max bound | 🟡 | **🟢-rank1** (formally closed via `OperatorNormBound.toJetTowerUniformDeltaMax`) / 🟡-multi-rank (residual conjecture) | §10 |
| **17a** — pentagon UV verification | 🟡 | 🟢 structurally addressed (formal-chain `pentagon_uv_commutation` theorem) | §11 |
| **17b** — descent sharpness on pairs | 🟡 | 🟡 residual; depth-2 cap witnessed by the absence of triple-form theorem | §11 |
| **18a** — `conj:mass-endomorphism` closed form | 🟡 | 🟡 (closed-form open math; class-axiomatised `vol_eq` field, `fullMass_eq_volume` no-`sorry`) | §12 |

### Cluster-by-cluster audit links

| Cluster | Audit § | Files moved/created in formal chain (`lean/QOU/`) |
|---------|---------|---------------------------------------------------|
| §1 — wall breaches | [§1](2026-05-03-pre-archimedean-proof-audit.md#§1-—-lean-wall-breaches) | (Pre/Arch namespace splits across 16 stub files) |
| §7 — bridge sharpening | [§7](2026-05-03-pre-archimedean-proof-audit.md#§7-—-sharp-bridge-audit-2026-05-03-follow-up) | `BraidKnot/PhiQTowerAlgebraicStratification.lean` (upgraded from `: True := trivial`) |
| §8 — motivic descent layer | [§8](2026-05-03-pre-archimedean-proof-audit.md#§8-—-sharp-step-6-audit-motivic-descent-layer) | `AlgebraicSubstrate/MotivicSubstrate.lean`, `LiftingDescent/MotivicGaloisCharacter.lean`, `LiftingDescent/MotivicPerpetualObstruction.lean` |
| §9 — GS-residue cluster | [§9](2026-05-03-pre-archimedean-proof-audit.md#§9-—-sharp-step-13-audit-gs-residue--spectral-sequence-cluster) | `BraidKnot/{ConfinementLevel,GBSpectralSequence,GBResidueSpectralSum,GradedTraceResidueSplit,ResidueAtRoot}.lean`; upgraded `GradedMarkovTraceFromGSFiltration.lean` |
| §10 — DB filtration | [§10](2026-05-03-pre-archimedean-proof-audit.md#§10-—-sharp-step-14-audit-db-filtration--δ_max-cluster) | `MassEndomorphism/DeltaMaxUniformBound.lean`, `LiftingDescent/DirectLimitAlgebra.lean`, `BraidKnot/JetTowerUniformDeltaMax.lean` |
| §11 — pentagon UV / Markov-pair | [§11](2026-05-03-pre-archimedean-proof-audit.md#§11-—-sharp-step-17-audit-pentagon-uv--markov-pair-cluster) | `Hecke/MarkovTraceProduct.lean`, `Hecke/MarkovPairZ2.lean` |
| §12 — mass endomorphism conjecture | [§12](2026-05-03-pre-archimedean-proof-audit.md#§12-—-sharp-step-18-audit-mass-endomorphism-cluster) | `MassEndomorphism/MassEndomorphismConjecture.lean` |
| §13 — cosimplicial gluing | [§13](2026-05-03-pre-archimedean-proof-audit.md#§13-—-sharp-step-7-audit-cosimplicial-gluing-cluster) | `LiftingDescent/CosimplicialCrossedGroupoid.lean`, `Torsion/DescentCondition.lean`, `Torsion/GlobalGluing.lean` |

### Headline change

Of the **6 named gaps** in §C (6a, 13a, 14a, 17a/b, 18a), three
are now reduced to **mathematical-instance** problems whose Lean
infrastructure is in place (6a, 14a-multi-rank, 18a), three are
**structurally addressed** in the formal chain (13a, 14a-rank1,
17a), and one is **residual** without load-bearing impact (17b).
The `noncomputable opaque` count in pre-Arch cluster `prop:` blocks
is **0** after the audit (down from 6).  `bun run validate
quantum-observable-universe` passes on the audit branch.

The mathematical content of each remaining 🟡 gap is unchanged —
these are honest open problems about the QOU substrate, the multi-
rank SDP, the closed-form mass-endomorphism, etc.  The audit's
contribution is **cleanly separating the conjectural inputs from
the conditional theorems**: each open conjecture is now an
explicit class field, each downstream theorem is conditional on
the right typeclass instance, and any concrete instance proof
will discharge every downstream consequence automatically via
typeclass resolution.
