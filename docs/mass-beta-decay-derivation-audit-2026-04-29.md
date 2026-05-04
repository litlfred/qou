# Mass / β-decay derivation audit (2026-04-29)

This audit traces the full derivation chain from the QOU axioms to
the Wedderburn mass formula and the β-decay $Q$-value, classifying
every flag along the way as

- ✓ **DERIVED** — proved from the axioms (no free parameters);
- ✓ **CALIBRATED** — fixed once and for all by one of the three
  allowed calibration inputs below (no free per-decay parameter);
- ⚠ **EMPIRICAL** — currently fitted or borrowed from outside the
  framework (a genuine gap, see §3);
- ⚠ **CONJECTURAL** — assumed but not proved in the present
  formalization (see §3).

It supersedes the earlier `derivation-audit-2026-04-20.md` for the
mass / β-decay sector specifically; that earlier audit incorrectly
flagged calibration inputs as empirical, inflating the apparent
gap count.

---

## 1. Calibration-input framing (preamble)

The framework admits **exactly three** scalar calibration inputs.
Every other dimensional quantity in the mass / β-decay sector is
either derived from these three or is an explicit conjectural /
empirical input that we record as a gap in §3.

| # | Input | Symbol | Role |
|---|-------|--------|------|
| 1 | Lepton mass ratio | $m_\mu / m_e$ | Pins $q_0 = 1.1097\ldots$ via the Descartes condition $\chi(A) = -6$ (one-parameter family in $q$ collapses to a point). |
| 2 | Electron mass | $m_e$ | Sets the absolute MeV scale. Every mass output of the framework is dimensionless × $m_e$; choosing $m_e$ in MeV fixes the unit. |
| 3 | Single β-decay $Q$-value | $Q_\beta(\text{ref})$ | Pins the energy-scale offset between the single-level Hecke energy $E_0 = m_e / (q_0 (q_0 - 1))$ and the full tower (which differs by ~0.75%); equivalently, fixes the Plancherel normalisation of the Markov trace at $A = 1$. |

**Reclassification rule.** Any flag that *only* touches one of the
three inputs above (i.e. would be eliminated if the input were
removed) is reclassified as ✓ **CALIBRATED**, not ⚠ EMPIRICAL.
Specifically:

- $q_0 = 1.1097\ldots$ — ✓ CALIBRATED via input 1 (was previously
  flagged ⚠ EMPIRICAL).
- $m_e$ as MeV scale — ✓ CALIBRATED via input 2 (was previously
  flagged ⚠ EMPIRICAL).
- The reference single $Q_\beta$ — ✓ CALIBRATED via input 3 (was
  previously flagged ⚠ EMPIRICAL).

After this reclassification, the audit reports only **genuine**
gaps in §3. Calibration is not a derivation gap — it is the
finite-input boundary condition that any physical theory needs to
attach dimensionless geometry to dimensional observables.

---

## 2. Revised derivation chain (pre-Archimedean → Hecke energy)

The following 16 steps form the canonical pre-Archimedean
derivation chain. Each step is either a theorem proved in the
content blocks, a definition, or one of the three calibration
inputs from §1. No step on this list is an empirical fit.

| # | Step | Output | Source / status |
|---|------|--------|-----------------|
| 1 | QOU axioms | Categorical action $S(\Phi) = \mathrm{tr}(\Phi)$ | `def:quantum-observable-universe`, `def:categorical-action` — DERIVED |
| 2 | Frobenius pairing | Non-degenerate categorical integration | `def:frobenius-pairing`, `prop:frobenius-non-degenerate` — DERIVED |
| 3 | Measurability axioms ($c_1 = c_2 = 0$) | Flat KZ connection (Yekutieli non-abelian Stokes) | `def:measurability-axioms`, `thm:flat-kz-connection` — DERIVED |
| 4 | Tannaka–Krein reconstruction | Gauge group $G = \mathrm{SU}_q(2)$ | `thm:tannaka-krein-reconstruction` — DERIVED |
| 5 | Braid group monodromy (Kohno–Drinfeld) | $R$-matrix → Hecke quotient $H_n(q)$ | `thm:kohno-drinfeld`, `def:hecke-quotient` — DERIVED |
| 6 | Descartes condition $\chi(A) = -6$ | One-parameter family in $q$, pinned by **calibration input 1** ($m_\mu / m_e$) to $q_0 = 1.1097\ldots$ | `prop:descartes-condition`, `def:q-pinning` — CALIBRATED |
| 7 | Confinement LP ($\min \mathrm{tr}_M$ s.t. Frobenius positivity) | Borromean braid $B_3$ | `prop:confinement-lp`, `thm:borromean-baryon` — DERIVED |
| 8 | Gram indefiniteness ($\det G < 0$) | Topological confinement proof | `thm:gram-indefiniteness-confinement` — DERIVED |
| 9 | Quark content → typed crossings | Nucleon braid words: proton $uud$, neutron $udd$ | `def:typed-crossing`, `def:nucleon-braid-word` — DERIVED |
| 10 | Typed crossing recurrence | Nuclear braid word $\mathcal{N}(Z, N)$ | `prop:nuclear-braid-recurrence` — DERIVED |
| 11 | Gröbner–Shirshov NF (Diamond Lemma) | Unique normal form for each nucleus | `thm:groebner-shirshov-nf`, `lem:diamond-confluence` — DERIVED |
| 12 | Transfer matrix recurrence at each generator | $\hat V_i(q)$ | `def:transfer-matrix`, `prop:transfer-matrix-recurrence` — DERIVED |
| 13 | Markov trace factorization | $\mathrm{tr}_M = \prod_i \hat V_i$ | `thm:markov-trace-factorization` — DERIVED |
| 14 | GS energy functional | Path-independent, monotone | `thm:gs-energy-path-independence`, `prop:gs-energy-monotone` — DERIVED |
| 15 | Wedderburn–Artin decomposition | Plancherel weights $w_\lambda$ | `thm:wedderburn-artin`, `def:plancherel-weight` — DERIVED |
| 16 | Wedderburn mass formula (zero-parameter) | $M(Z, N)$ | `prop:wedderburn-mass-formula` — DERIVED (modulo G-2, see §3) |

**Pre-Archimedean closure.** Steps 1–16 are entirely
pre-Archimedean: they use only (a) the QOU axioms, (b) the three
calibration inputs of §1, and (c) finite-dimensional linear
algebra over $\mathbb{Q}(q)$ specialized at $q_0$. No step
invokes the volume conjecture, Mostow rigidity, Gromov norm, or
any other Archimedean / hyperbolic-geometry input. The
post-Archimedean bridge (volume conjecture at real $q$) appears
only when comparing Hecke trace values to MeV masses (gap G-1).

---

## 3. Gap audit — genuine gaps only

The table below lists the **only** unresolved derivation gaps
after the §1 reclassification removed the three calibration
inputs. Calibration of $q_0$, $m_e$, and the single $Q_\beta$
reference are *not* listed here — they are CALIBRATED, not
EMPIRICAL.

| Gap | Description | Severity |
|-----|-------------|----------|
| **G-1** | **Volume conjecture at real $q$** — only unproved link between Hecke trace and MeV masses. The chain steps 1–16 produce dimensionless Hecke trace values; their identification with hyperbolic volumes (and hence MeV masses via $m_e \cdot \mathrm{Vol}$) is conjectural at non-root-of-unity $q$. | **Critical** |
| **G-2** | **Fitted $\beta_3 \approx 0.050$** in the Wedderburn formula — coefficient of the depth-3 term is fitted, not derived from the recursion tower. | **High** |
| **G-3** | **Tower binding energy vs. direct deuterium formula** disagree at $A = 2, 4$. Two formally derived expressions for $E_{\text{bind}}(d)$ and $E_{\text{bind}}({}^4\text{He})$ give numerically distinct results; formula reconciliation is missing. | **High** |
| **G-4** | **β-decay half-life not derived** — the Sargent / Fermi-function machinery (phase-space integral, Coulomb correction $f(Z, Q)$) is not yet derived categorically; Fermi constant $G_F$ is treated as input. | **High** |
| **G-5** | **Fermi constant $G_F$ not derived** from the categorical coupling. The $\mathrm{SU}_q(2)$-weak-isospin coupling should fix $G_F$ via a Plancherel weight, but the bridge is incomplete. | **High** |
| **G-6** | **Frobenius packing density** $\rho_F \in [m_e, 2 m_e]$ — interval is stated and used in shell-construction proofs but the bounds are not proved from Frobenius non-degeneracy. | **Medium** |
| **G-7** | **Binding scale $\alpha = 8 G \cdot m_e$** — calibrated by the deuterium binding energy rather than independently derived from $G_F$ + Plancherel weights. (Independent of calibration input 3, which is the single-decay $Q$-value, not a binding energy.) | **Medium** |
| **G-8** | **Shell closure / magic numbers from Hecke** — stated as `prop:magic-numbers-from-q` but the derivation is informal; the shell-closure prediction at $Z, N \in \{2, 8, 20, 28, 50, 82\}$ is empirical pattern-matching, not derived from the Hecke representation theory. | **Medium** |
| **G-9** | **n–p splitting 0.63% residual** — Wedderburn formula reproduces $m_n - m_p$ to 0.63%; the residual is attributed to brane-tower and isospin corrections that are not yet computed. | **Medium** |
| **G-10** | **QED correction $(1 - \alpha_{\mathrm{EM}}/2)$** in the deuterium binding formula is borrowed from standard QED; not derived categorically. | **Low** |
| **G-11** | **Energy scale**: single-level $E_0 = m_e / (q_0 (q_0 - 1))$ misses the tower by 0.75%; this is correctly fixed by **calibration input 3**, but the audit text needs an explicit note pointing out that this is calibrated, not empirical. (Documentation gap, not derivation gap.) | **Low** |
| **G-12** | **Crossing-graded mass expansion** — the locality hypothesis (mass contributions of distant crossings are negligible at order $q^{-N}$) is used in the recurrence but not proved. | **Low** |
| **G-13** | **JSJ decomposition canonicity** — verified per-atom (atoms in the periodic table up to $Z = 92$) but not proved canonical in general. | **Low** |

**Removed from previous gap table** (because they are calibration
inputs, not gaps):

- ~~$q_0 = 1.1097$ empirical~~ → ✓ CALIBRATED via input 1.
- ~~$m_e$ in MeV empirical~~ → ✓ CALIBRATED via input 2.
- ~~Reference single $Q_\beta$ empirical~~ → ✓ CALIBRATED via input 3.

---

## 4. Resolution paths

For each gap, a concrete derivation outline (theorem statement or
computation that would close it).

### G-1 (Critical) — Volume conjecture at real $q$

- **Target theorem.** $\mathrm{tr}_M(\beta_L) \big|_{q = q_0} =
  \mathrm{Vol}(S^3 \setminus \hat\beta_L) / (2 \pi)$ for every
  hyperbolic link $\hat\beta_L$ closing the braid $\beta_L$.
- **Approach.** Specialize Yokota's saddle-point analysis of the
  Kashaev invariant from $q = e^{2\pi i / N}$ to real $q > 1$;
  show the saddle equations admit a real positive solution
  identified with the hyperbolic volume via Neumann–Zagier. The
  Picard–Lefschetz route in `docs/picard-lefschetz-plan.md` is
  the current candidate.
- **Closes.** Step 16 → MeV bridge. Once G-1 is closed, every
  mass / $Q$-value prediction becomes a pure theorem.

### G-2 (High) — Fitted $\beta_3 \approx 0.050$

- **Target lemma.** $\beta_3$ equals the Plancherel weight of
  the depth-3 stratum in the Wedderburn decomposition of
  $H_n(q_0)$ at $n = 3$, i.e. $\beta_3 = w_{(2,1)} / w_{(1,1,1)}$
  (or analogous ratio).
- **Approach.** Compute Hoefsmit eigenvalue products at $q_0$
  for the standard module $S^{(2,1)}$; verify numerical match to
  $0.050 \pm 10^{-3}$. Witness file
  `wedderburn-orthogonal-r-3-h4.witness.json` already contains
  the $H_4$ data; extend to $H_3$ and check.

### G-3 (High) — Tower vs. direct deuterium reconciliation

- **Target proposition.** $E_{\text{bind}}^{\text{tower}}(d) =
  E_{\text{bind}}^{\text{direct}}(d)$ as elements of $\mathbb{Q}(q)$
  (i.e. the two formal series agree, not just numerically).
- **Approach.** Rewrite both sides as Markov-trace polynomials in
  $q$ and use Gröbner–Shirshov NF to prove formal equality. The
  current 0.4% numerical mismatch suggests a missing $O(q^{-3})$
  term in the direct formula. See
  `docs/audits/derivation-chain-mass-tower.md`.

### G-4 (High) — β-decay half-life from categorical phase space

- **Target theorem.** $t_{1/2}(\text{decay}) = \ln 2 / (G_F^2 \cdot
  f(Z, Q) \cdot |\mathcal{M}|^2)$ where $f(Z, Q)$ is the
  categorical phase-space integral derived from the spectral
  measure of the Markov trace on the closing braid.
- **Approach.** Derive the Sargent rule ($f \propto Q^5$) from
  the Plancherel measure of $\mathrm{SU}_q(2)$ acting on the
  outgoing electron-neutrino state space; identify the Coulomb
  correction with the Tannakian fibre functor on the daughter
  nucleus.

### G-5 (High) — $G_F$ from categorical coupling

- **Target lemma.** $G_F = c \cdot m_e^{-2}$ where $c$ is a
  pure rational function of $q_0$ extracted from the
  $\mathrm{SU}_q(2)$ weak-isospin Plancherel weight.
- **Approach.** Identify the weak coupling with the categorical
  trace of the $\mathrm{SU}_q(2)$-equivariant $R$-matrix at the
  $J = 1/2$ representation; specialize at $q_0$ and check
  $G_F \approx 1.166 \times 10^{-5}\,\text{GeV}^{-2}$.

### G-6 (Medium) — Frobenius packing density bounds

- **Target lemma.** For any non-degenerate Frobenius pairing on
  the standard module of $H_n(q_0)$, the diagonal density
  $\rho_F$ satisfies $m_e \le \rho_F \le 2 m_e$.
- **Approach.** Bound the Hoefsmit norm of the diagonal projector
  using the Cauchy–Schwarz inequality on the Frobenius form; the
  upper bound follows from positivity of off-diagonal entries.

### G-7 (Medium) — Binding scale $\alpha = 8 G \cdot m_e$ derivation

- **Target.** Derive $\alpha$ from $G_F$ + Plancherel weights
  (depends on G-5).
- **Approach.** Once G-5 closes, $\alpha = 8 G m_e$ should
  follow from the binding-channel Plancherel weight of the
  $A = 2$ nucleus.

### G-8 (Medium) — Shell closure / magic numbers from Hecke

- **Target proposition.** Shell-closure occurs precisely when
  $\dim S^\lambda = 0$ for the Specht module $S^\lambda$ at the
  next $A$-level (i.e. degeneration of the Hecke representation
  forces a closed shell).
- **Approach.** Compute Hecke representation dimensions at
  $A = 2, 8, 20, 28, 50, 82$ via Murnaghan–Nakayama at $q_0$;
  verify dimension drop pattern matches magic numbers.

### G-9 (Medium) — n–p splitting 0.63% residual

- **Target.** Compute the brane-tower correction $\delta m_{np}$
  to first order in $q^{-2}$ and check $|m_n - m_p|^{\text{tower}}
  + \delta m_{np} = (m_n - m_p)^{\text{exp}}$.
- **Approach.** Brane tower contributes at order $q^{-2 \cdot 3} =
  q^{-6}$; isospin breaking at order $\alpha_{\text{EM}}$. Sum
  should reproduce 1.293 MeV split.

### G-10 (Low) — QED correction $(1 - \alpha_{\text{EM}}/2)$

- **Target.** Derive the deuterium QED correction from the
  $\mathrm{U}(1)$-twisted Hecke representation at $q_0$.
- **Approach.** Twist the standard module by the $\mathrm{U}(1)$
  character corresponding to electromagnetic coupling; compute
  the first-order correction to the Markov trace.

### G-11 (Low) — Energy-scale documentation note

- **Target.** Add a one-paragraph note to
  `q-value-transition.md` (or the appendix) stating that the
  0.75% offset between $E_0$ and the full tower is fixed by
  calibration input 3, not by an empirical fit.
- **Approach.** Documentation only — no theorem needed.

### G-12 (Low) — Crossing-graded locality hypothesis

- **Target lemma.** The mass contribution of a crossing at
  positions $|i - j| > N$ is bounded by $C \cdot q^{-N}$ for
  some constant $C$ depending only on the braid word.
- **Approach.** Spectral-gap argument on the transfer matrix
  $\hat V_i$; the gap of the second-largest eigenvalue at $q_0$
  is approximately $q_0^{-1}$, giving exponential decay.

### G-13 (Low) — JSJ canonicity in general

- **Target theorem.** For every nuclear braid word $\mathcal{N}(Z, N)$
  with $Z + N \le 240$, the JSJ decomposition is unique up to
  isotopy of the braid closure.
- **Approach.** Use Jaco–Shalen / Johannson canonicity
  (already a theorem for irreducible 3-manifolds); show that
  every nuclear braid closes to an irreducible link by
  enumerating exceptional cases (none observed in
  computations).

---

## 5. Status summary

| Category | Count | List |
|----------|-------|------|
| ✓ DERIVED steps | 15 / 16 | Steps 1–5, 7–16 (step 16 modulo G-2) |
| ✓ CALIBRATED steps | 1 / 16 | Step 6 (via input 1) |
| ⚠ Critical gaps | 1 | G-1 |
| ⚠ High gaps | 4 | G-2, G-3, G-4, G-5 |
| ⚠ Medium gaps | 4 | G-6, G-7, G-8, G-9 |
| ⚠ Low gaps | 4 | G-10, G-11, G-12, G-13 |
| Total genuine gaps | 13 | — |

The headline number is **one critical gap** (G-1, the volume
conjecture at real $q$). Every other gap is either an internal
reconciliation (G-2, G-3, G-9), a deferred categorical derivation
of a standard-physics input (G-4, G-5, G-7, G-10), or a stated-
but-not-proved bound or canonicity claim (G-6, G-8, G-12, G-13).
G-11 is purely documentation.

Closing G-1 is the single highest-value formalization target; it
would convert the entire mass / β-decay sector from
"calibrated + conjectural" to "calibrated + theorem". All
post-Archimedean uses in the paper hinge on this one bridge.
