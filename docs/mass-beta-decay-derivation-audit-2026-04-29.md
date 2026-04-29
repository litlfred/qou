# Mass, Beta Decay & Binding Energy — Derivation Audit
*Branch: `copilot/audit-mass-and-beta-decay` | Date: 2026-04-29*

---

## Executive Summary

This audit traces every mass, beta-decay Q-value, binding energy, and
predicted nuclear observable back to the pre-archimedean categorical
framework.  Items are flagged with one of:

| Flag | Meaning |
|:----:|:--------|
| ✓ | Categorically derived; no free parameters |
| ⚠ EMPIRICAL | Uses CODATA / AME data as input |
| ⚠ FITTED | Has one or more free numerical parameters |
| ⚠ CONJECTURAL | Rests on an unproven conjecture |
| ❌ MISSING | Derivation absent; gap in the chain |

---

## Part A — Full Algebraic Derivation Chain (Pre-Archimedean → Hecke Energy)

### A.1  Categorical Action

**Block**: `def:categorical-action`

The starting point is the QOU $(\mathbf{C}, A, \tau)$ with:
- $A$ a Frobenius–Hopf algebra in a rigid monoidal category $\mathbf{C}$,
- $\tau: \mathbf{C} \to \mathbf{Vect}_R$ a faithful fibre functor.

The categorical action of an endomorphism $\Phi \in \mathrm{End}_\mathbf{C}(A)$ is:

$$
  \mathcal{S}(\Phi)
  = \mathrm{ev}_A \circ (\mathrm{id}_{A^\vee} \otimes \Phi) \circ \mathrm{coev}_A
  = \mathrm{tr}(\Phi).
$$

**Status: ✓**  Established from the rigid monoidal axioms alone.

---

### A.2  Frobenius Pairing and Non-Degenerate Integration

**Block**: `def:frobenius-pairing`, `def:quantum-observable-universe`

The QOU measurability axiom requires:
1. $\int_A: A \to \mathbf{1}$ induces a non-degenerate pairing $(a,b) \mapsto \int_A ab$, i.e. $A \cong A^\vee$.
2. No hidden global symmetries: $\mathrm{Hom}_\mathbf{C}(\mathbf{1}, \mathrm{Ad}(A)) = 0$.
3. Chern classes vanish: $c_1(\mathrm{Ad}(A)) = c_2(\mathrm{Ad}(A)) = 0$.

The Frobenius pairing is the Markov trace at the categorical level.

**Status: ✓**

---

### A.3  Non-Abelian Stokes Theorem → Flat KZ Connection

**Block**: `rem:yekutieli-stokes-remark`

The vanishing $c_1(\mathrm{Ad}(A)) = 0$ removes the primary topological
obstruction to flatness of the adjoint bundle.  Combined with the
categorical rigidity of the Frobenius–Hopf algebra (which confines the
connection to the instanton locus), this implies:

$$
  F_\nabla = 0 \quad \text{(flat categorical connection)}.
$$

By Yekutieli's nonabelian Stokes theorem \cite{yekutieli2015}, the
categorical volume $\varepsilon$ (the volume constraint epimorphism
$\Lambda^2 V \twoheadrightarrow \mathbf{1}$) is well-defined precisely
because of this flatness.

The additional condition $c_2(\mathrm{Ad}(A)) = 0$ ensures the volume
form acquires no topological phases under transport — the adjoint bundle
is anomaly-free.

**Status: ✓**  Established via Kohno–Drinfeld theorem for the monodromy.

---

### A.4  Tannaka–Krein Reconstruction → G = SU_q(2)

**Blocks**: `thm:tannaka-krein-isomorphism`, `def:quantum-universe-su2`

The Tannaka–Krein reconstruction theorem for the triple $(\mathbf{C}, A, \tau)$
with the volume constraint $\varepsilon: \Lambda^2 V \twoheadrightarrow \mathbf{1}$
uniquely reconstructs the symmetry group as:

$$
  G = \mathrm{Aut}^\otimes(\tau) \cong \mathrm{SU}_q(2).
$$

The braid group $B_n$ enters as the fundamental group of the
configuration space $X_n = \{(w_1, \ldots, w_n) \in \mathbb{C}^n : w_i \neq w_j\}$,
with the KZ monodromy representation factoring through the Iwahori–Hecke
algebra $H_n(q)$.

**Status: ✓**

---

### A.5  Knot Decomposition: Braid Group → Hecke Algebra

**Blocks**: `def:braid-group`, `prop:nuclear-groebner-reduction`

Every braid $\beta \in B_n$ maps to $H_n(q)$ via the Hecke quotient
$\mathbb{Z}[q^{\pm 1}][B_n] \to H_n(q)$ using the Skein relation:

$$
  \sigma_i - \sigma_i^{-1} = q - q^{-1}.
$$

The Gröbner–Shirshov basis $G$ for $H_A(q)$ (established in the
companion paper `unital-groebner-bases`) gives:
1. **Hecke**: $\sigma_i^2 = (q - q^{-1})\sigma_i + 1$
2. **Yang–Baxter**: $\sigma_i \sigma_{i+1} \sigma_i = \sigma_{i+1} \sigma_i \sigma_{i+1}$
3. **Far commutativity**: $\sigma_i \sigma_j = \sigma_j \sigma_i$ for $|i-j| \geq 2$

Uniqueness of the normal form $\mathcal{N}(Z,N)$ follows from the
Bergman Diamond Lemma.

**Status: ✓**  (GS basis established in `ugb` Lake package.)

---

### A.6  Weierstrass / Descartes Condition → Substrate Parameter q

**Block**: `prop:descartes-elliptic-curve`, `prop:local-substrate-q`

The Descartes condition on the elliptic curve $\mathcal{E}_q$ associated
to the volume constraint yields the fixed-point equation:

$$
  (1 - q^{-1})^2 = \frac{\mathrm{Vol}(4_1)}{m_\mu / m_e}
  \quad\Longrightarrow\quad q_0 = 1.1097 \pm 0.001.
$$

where $\mathrm{Vol}(4_1) = 3\,\mathrm{Cl}_2(\pi/3) \approx 2.0299$ is the
hyperbolic volume of the figure-eight knot (exact algebraic constant)
and $m_\mu/m_e$ is the muon–electron mass ratio.

**⚠ EMPIRICAL**: $m_\mu/m_e = 206.768..$ is taken from CODATA 2022.
This is the **only** non-categorical external input into the substrate
parameter.  The rationale for pinning $q$ to the figure-eight knot volume
divided by the muon mass ratio is:
- The figure-eight knot $4_1$ is the simplest hyperbolic knot (unique in its volume category).
- The muon is identified with the $4_1$ particle state in the knot–particle
  dictionary: $m_\mu/m_e = \mathrm{Vol}(4_1)/\hbar_q^2$.
- **Gap**: The categorical identification $m_\mu = \mathrm{Vol}(4_1) \cdot \rho_q$
  (with $\rho_q = 1/\hbar_q^2$) is the **volume conjecture at real $q$**
  (see Gap G-1 below), not a theorem.

**Status: ⚠ EMPIRICAL + ⚠ CONJECTURAL**

---

### A.7  Confinement and Borromean Topology

**Blocks**: `prop:confinement-lp`, `prop:confinement-topological`,
`prop:confinement-nucleon-unit`

The confinement operator for a nucleon (3-quark system in $H_3(q)$) is
selected by:

1. **LP confinement**: Minimize the categorical action $\mathrm{tr}_M(\Phi)$
   subject to the Frobenius positivity constraint $G\vec{x} \geq 0$
   (where $G$ is the $6\times6$ Gram matrix) and a net constraint
   $\sum x_i = n_\mathrm{target}$.

2. The LP solution selects $\mathcal{B}_3 = (\sigma_0 \sigma_1^{-1})^3$
   as the confinement operator — the Borromean braid.

3. **Gram indefiniteness** ($\det G < 0$, eigenvalue $\approx -0.956$)
   shows confinement is **topological**, not energetic: the global minimum
   is at $\mathrm{tr}_M = 0$ (massless), and the Borromean braid is the
   least unstable confined state at the LP vertex.

**⚠ CONJECTURAL / NUMERICAL**: The LP is solved numerically.  The
$n_\mathrm{target}$ values ($\approx 1.000$ for proton, $\approx 0.811$
for neutron) are derived from the quark content but require an LP solver.
The selection of $\mathcal{B}_3$ as the unique nucleon operator is proved
via LP duality and Gram indefiniteness — these are exact algebraic
arguments, but the LP itself is numerical.

**Status: ✓** (algebraic argument via LP duality; numerical verification)

---

### A.8  Nucleon Quark → Braid Word Assignment

**Block**: `def:categorical-proton`, `def:categorical-neutron`,
`prop:confinement-operator-selection`

The proton $\mathfrak{p} = \mathfrak{u}\mathfrak{u}\mathfrak{d}$ and neutron
$\mathfrak{n} = \mathfrak{u}\mathfrak{d}\mathfrak{d}$ are assigned braid words
in $H_3(q)$ by the confinement operator selection:

$$
  \mathfrak{p}
  = \mathcal{B}_3 \cdot [\sigma_0(\mathfrak{u}\mathfrak{u})]
    \cdot [\sigma_1 - \tfrac{h}{2}](\mathfrak{u}\mathfrak{d})
    \cdot [\sigma_0 - \tfrac{h}{2}](\mathfrak{u}\mathfrak{d})
$$

$$
  \mathfrak{n}
  = \mathcal{B}_3 \cdot [\sigma_0 - \tfrac{h}{2}](\mathfrak{u}\mathfrak{d})
    \cdot [\sigma_1 - h](\mathfrak{d}\mathfrak{d})
    \cdot [\sigma_0 - \tfrac{h}{2}](\mathfrak{u}\mathfrak{d})
$$

The crossing signs follow from:
- $\mathfrak{u}\mathfrak{u}$ pair → $\sigma$ (eigenvalue $+q$, positive crossing)
- $\mathfrak{d}\mathfrak{d}$ pair → $\sigma^{-1}$ (eigenvalue $-q^{-1}$, negative)
- $\mathfrak{u}\mathfrak{d}$ mixed pair → $\frac{1}{2}(\sigma + \sigma^{-1})$

**Status: ✓** (crossing signs are exact algebraic consequences of Hecke
eigenvalues; the braid word is uniquely determined by quark content and
the confinement LP.)

---

### A.9  Nuclear Braid Word Construction

**Block**: `prop:nuclear-groebner-reduction`

The nucleus $\mathcal{A}(Z,N)$ with $A = Z+N$ nucleons has a raw braid
word in $B_A$:

$$
  \mathcal{N}_\mathrm{raw}(Z,N)
  = \prod_{1 \leq i < j \leq A} \sigma_i^{\epsilon(i,j)}
$$

where $\epsilon(i,j) \in \{+1, -1, 0\}$ depends on nucleon types, and
mixed crossings use $\frac{1}{2}(\sigma + \sigma^{-1}) = \sigma - \frac{h}{2}$.

The GS normal form $\mathcal{N}(Z,N) = r(\mathcal{N}_\mathrm{raw}, G)$ is
unique by the Diamond Lemma.

**Status: ✓**

---

### A.10  Transfer Matrix Product and Jet Expansion

**Block**: `prop:generator-volume-decomposition`, `thm:markov-trace-factorization`

At each generator $\sigma_i$, the $k_i = A-i-1$ crossings with later
strands reduce to $a_i \sigma_i + b_i$ via the recurrence:

$$
  a_{k+1} = a_k c_j (q-q^{-1}) + a_k d_j + b_k c_j, \quad
  b_{k+1} = a_k c_j + b_k d_j.
$$

The Markov trace factors exactly as:

$$
  \mathrm{tr}_M(\mathcal{N}(Z,N))
  = \prod_{i=0}^{A-2} (z \cdot a_i + b_i)
  = \prod_{i=0}^{A-2} \hat{V}_i(q).
$$

This is an exact algebraic identity.  The **jet expansion** interprets
the transfer matrix product as the exact $k_i$-jet of a formal
power series in crossing count — every order through $k_i = A-i-1$ is
computable in $\binom{A}{2}$ steps.

**Status: ✓**

---

### A.11  Gröbner–Shirshov Energy Functional

**Block**: `thm:groebner-shirshov-energy`

The energy functional on $H_A(q)$:

$$
  E(\xi) = \sum_{w \in B} |c_w(q)| \cdot \ell(w)
$$

is path-independent (Diamond Lemma: all reduction paths lead to the
same NF) and changes only under Hecke reductions:

$$
  \Delta E_\mathrm{step} = |c| \cdot |q - q^{-1}| \quad > 0 \quad (\text{since } q > 1).
$$

**Status: ✓**  This is a theorem (proved via Bergman Diamond + GS basis).

---

### A.12  Wedderburn–Artin Decomposition and Plancherel Weights

**Block**: `prop:gram-weight-eigenstructure`, `thm:wedderburn-mass-formula`

The Hecke algebra $H_n(q)$ decomposes as:

$$
  H_n(q) \cong \bigoplus_{\lambda \vdash n} M_{d_\lambda}(R)
$$

with Plancherel weights:

$$
  w_\lambda = \frac{d_q(\lambda)^2}{[n]_q!}, \quad
  \sum_\lambda d_q(\lambda)^2 = [n]_q!.
$$

At $n = 3$: three blocks (sym $(3)$, std $(2,1)$, alt $(1,1,1)$) with
$w_\mathrm{sym} = w_\mathrm{alt} = 1/[3]_q! \approx 0.165$,
$w_\mathrm{std} = [2]_q^2/[3]_q! \approx 0.669$.

The full traced volume per generator is the Wedderburn-weighted sum:

$$
  \hat{V}_i^\mathrm{full}
  = w_\mathrm{sym} \cdot \lambda_i^\mathrm{sym}
  + w_\mathrm{std} \cdot \hat{V}_i^\mathrm{std}
  + w_\mathrm{alt} \cdot \lambda_i^\mathrm{alt}.
$$

**Status: ✓**

---

### A.13  Atomic Mass Formula (Wedderburn)

**Block**: `thm:wedderburn-mass-formula` (zero-parameter version)

$$
  \mathcal{M}(Z,N)
  = Z m_\mathfrak{p} + N m_\mathfrak{n} + Z m_e
  + \alpha \sum_i \ln|\hat{V}_i^\mathrm{full}|
$$

with binding scale $\alpha = m_e \cdot 8G$ (Catalan constant $G \approx 0.9160$,
$\mathrm{Vol}(\mathcal{B}_3) = 8G$ by the volume formula for the Borromean link).

- Zero-parameter formula (exact Wedderburn): mean error **0.146%**
- One-parameter formula ($\beta_3 \approx 0.050$, fitted): mean error **0.074%**

**Status: ✓ (zero-param)**,  **⚠ FITTED (one-param)**

See Gap G-2: $\beta_3$ is not derived.

---

### A.14  Nuclear Binding Energy (Tower)

**Block**: `prop:tower-binding-energy`

$$
  B(Z,N) = \sum_\lambda w_\lambda \cdot m_e \cdot \sum_i \ln|\Phi_q(\hat{V}_i^\lambda)|
$$

where $\Phi_q(x) = \prod_{k=1}^\infty |1 - q^{-k} x|^{-1}$ is the $q$-Pochhammer tower.

**Status: ✓ (formula)**  but see Gap G-3 for the absolute accuracy issues.

---

### A.15  Beta Decay Transfer Matrix and Q-Value

**Block**: `prop:beta-decay-transfer-matrix`, `thm:groebner-shirshov-energy`

The universal beta decay matrix is:

$$
  \Delta_\beta(q) = \tfrac{1}{2}(q - q^{-1}) \mathbb{I},
$$

an exact algebraic result.  The Q-value in log form:

$$
  \ln \frac{P_\mathrm{dau}(q)}{P_\mathrm{par}(q)}
  = \sum_i \ln \frac{\hat{V}_i^\mathrm{dau}}{\hat{V}_i^\mathrm{par}}.
$$

The **energy scale** connecting the dimensionless NF difference to MeV:

$$
  E_0 := \frac{m_e}{q_0(q_0 - 1)} = m_e \cdot c_q^2 \cdot \hbar_q \approx 4.186 \text{ MeV}.
$$

**⚠ EMPIRICAL**: Uses $m_e$ from CODATA.
**Status: ✓ (functional form)** | **⚠ EMPIRICAL (scale)**

---

### A.16  Beta Decay Half-Life

**Block**: (absent — see Gap G-4)

The Q-value and energy-release ΔE are computed.  The **half-life** is
mentioned as proportional to the inverse squared nuclear matrix element
$|\mathcal{M}_q|^2 \propto |\mathrm{tr}_M(\mathcal{N}_\mathrm{par} - \mathcal{N}_\mathrm{dau})|^2$,
but no full derivation exists connecting this to the observed half-life.

**Status: ❌ MISSING**

---

## Part B — Explicit Audit Flags

---

### G-1: Volume Conjecture at Real q (CRITICAL)

**Location**: `conj:mass-volume-factorization`, `prop:topological-mass-formula`,
`prop:local-substrate-q`

**The gap**: The equality $\mathfrak{m}(K) = \mathrm{Vol}(K)/\hbar_q^2$ —
which gives particle masses from hyperbolic knot volumes — is the
**volume conjecture at real q**.  The classical volume conjecture
(Kashaev; Murakami–Murakami) states a limit relation at $q = e^{2\pi i/N}$
as $N \to \infty$.  The paper applies this at *real* $q \approx 1.1097$,
which is an analytic continuation to the real axis.  This is:

1. Not a theorem (the classical conjecture is itself unproven for most knots).
2. Plausible (computational evidence: muon mass, proton mass, etc. match).
3. The foundation for ALL particle mass predictions.

**Consequence**: Every mass prediction is contingent on this conjecture.
The chain from categorical action → Hecke energy is solid, but the final
connection to MeV-scale particle masses requires this bridge.

**What is needed**: Either (a) a categorical proof that $\rho_q = 1/\hbar_q^2$
is the unique density consistent with the QOU axioms, or (b) an explicit
statement that the volume conjecture at real $q$ is an additional axiom
of the framework.

---

### G-2: Fitted Parameter β₃ in Wedderburn Mass Formula

**Location**: `thm:wedderburn-mass-formula`, `rem:atomic-braid-mass`

**The gap**: The "effective formula" uses $\beta_3 \approx 0.050$ (fitted),
described as compensating for "$\mathcal{B}_3$ dressing of hydrogen and
ordering effects in heavy nuclei."  This is **not derived** from the
categorical structure.

**Impact**: The fitted formula achieves 0.074% MAE (32 isotopes) vs.
0.146% for the exact zero-parameter formula.  The 0.074% is sometimes
quoted as the paper's accuracy, but it uses a free parameter.

**What is needed**: Either (a) derive $\beta_3$ from the brane-tower
correction or dressing of the Borromean base, or (b) be explicit that
the 0.074% figure uses a fitted parameter and report both.

---

### G-3: Absolute Binding Energy Accuracy

**Location**: `prop:tower-binding-energy`

**The gap**: The tower binding energy formula `prop:tower-binding-energy`
achieves small *mass* errors (0.071%) but has large *absolute binding
energy* errors for light nuclei:

| Atom | $B_\mathrm{pred}$ (MeV) | $B_\mathrm{obs}$ (MeV) | Rel. error |
|:----:|:---:|:---:|:---:|
| D | 4.92 | 2.22 | **+121%** |
| ⁴He | 19.41 | 28.30 | **−31%** |
| ⁷Li | 42.24 | 39.24 | +8% |
| ¹²C | 82.89 | 92.16 | −10% |
| ⁴⁰Ca | 317.38 | 342.05 | −7% |

The mass error is small because binding energy is a small fraction of
total mass ($B/M \lesssim 1\%$).  But the binding energy itself is
wrong by factors of 1–2 for the lightest nuclei.

**What is needed**: The deuteron binding energy IS correctly predicted
at 0.008% by `prop:deuterium-derived-binding` using a different
formula.  There is a **formula mismatch**: the tower formula and the
direct deuterium formula give different answers.  The reconciliation
between these two formulas is not documented.

---

### G-4: Half-Life Not Derived (CRITICAL)

**Location**: `thm:groebner-shirshov-energy`, beta decay blocks

**The gap**: The framework computes:
- The Q-value of beta decay (energy release) ✓
- The ΔE (Hecke energy difference between parent and daughter) ✓
- The beta decay matrix element in terms of Skein polynomial ratio ✓

But it does **NOT** derive the half-life.  The nuclear matrix element
$|\mathcal{M}_q|^2 \propto |\mathrm{tr}_M(\mathcal{N}_\mathrm{par} - \mathcal{N}_\mathrm{dau})|^2$
is given, but the Fermi golden rule requires:

$$
  T_{1/2} = \frac{\ln 2}{\Gamma}, \quad
  \Gamma \propto G_F^2 |\mathcal{M}_q|^2 Q^5 \cdot f(Z, Q)
$$

where $G_F$ is the Fermi constant (needs categorical derivation),
$Q^5$ is the phase-space factor, and $f(Z, Q)$ is the Fermi function
(Coulomb correction).

None of these connecting factors are derived from the categorical
framework.  The paper's beta decay blocks compute Q-values correctly
but cannot predict half-lives.

**What is needed**: Either derive $G_F$ from the categorical coupling
$\alpha_\mathrm{EM} = 1/(q \cdot [9]_q \cdot [10]_q)$ via the weak
mixing angle, or explicitly scope the framework to Q-values only.

---

### G-5: Fermi Constant / Weak Scale Not Derived

**Location**: (absent)

**The gap**: The Fermi constant $G_F \approx 1.166 \times 10^{-5}$ GeV$^{-2}$
sets the overall rate of weak decays.  The paper derives:
- $\alpha_\mathrm{EM} \approx 1/137$ from $1/(q \cdot [9]_q \cdot [10]_q)$ ✓
- The Q-value scale from $m_e/(q(q-1))$ ✓

But $G_F$ is **not derived**.  All half-life computations (present and
future) will require this.

---

### G-6: Frobenius Packing Density ρ_F ∈ {m_e, 2m_e}

**Location**: `rem:frobenius-packing-density`, `conj:mass-volume-factorization`

**The gap**: The rule that nuclear binding scales as $\rho_F \cdot V_\mathrm{hyp}$
with $\rho_F = m_e$ (single-chirality) or $\rho_F = 2m_e$ (CPT-saturated)
is stated as a first-principles derivation from the Frobenius structure.
However, `mass-volume-factorization.md` acknowledges:

> "The density $\rho_F(P_i)$ is determined locally by the Wedderburn
> profile of $P_i$ — **stated but not derived from first principles**."

The "topological triggers" (two-body links → $m_e$, three-body Borromean → $2m_e$)
are supported by computational evidence for light nuclei but not proved in general.

**What is needed**: A general proof that the alt Wedderburn block is
activated if and only if the link is three-body entangled (Borromean-type),
following from the Hecke algebra representation theory.

---

### G-7: α = m_e × 8G Binding Scale

**Location**: `prop:deuterium-derived-binding`, `prop:neutron-proton-splitting`,
`thm:wedderburn-mass-formula`

**The gap**: The binding scale $\alpha = m_e \cdot \mathrm{Vol}(\mathcal{B}_3) = m_e \cdot 8G$
(where $G$ is Catalan's constant) appears in multiple places:
- Deuterium binding energy (correctly predicts 2.225 MeV)
- Neutron–proton mass splitting (0.63% error)
- Atomic mass formula

The identification $\mathrm{Vol}(\mathcal{B}_3) = 8G$ is an exact theorem
(Thurston).  But the claim that this volume equals the nuclear binding
scale requires the volume conjecture at real $q$ (see G-1).

The scale is *calibrated* by deuterium binding, not *derived* independently
of it.  The 0.63% residual in the n–p splitting and the agreement of
deuterium binding are independent checks, but the initial calibration
uses CODATA $m_e$.

**Status: ⚠ EMPIRICAL** (calibrated via $m_e$; functionally derived given G-1)

---

### G-8: Shell Closure Conjecture Underpins Pairing Term

**Location**: `conj:shell-closure-nf-term-count`,
`conj:palindromicity-orbital-type`, `prop:q-integer-mass-formula`

**The gap**: The pairing term $\delta_P = [3]_q [7]_q m_e$ and shell
correction $\delta_S = [2]_q^2 [3]_q m_e$ in the q-integer BW formula
rest on:

1. **`conj:shell-closure-nf-term-count`**: The Hecke algebra shell gap —
   no $Z$ has $\gamma \in (1.4, 3.0)$ where $\gamma$ is the NF term count
   growth rate.  Computationally verified; not proved.

2. **`conj:palindromicity-orbital-type`**: The paired state has palindromic
   NF histogram.  Computationally verified; not proved.

The magic numbers $\{2, 8, 20, 28, 50, 82, 126\}$ in the shell correction
are argued to emerge from the Chebyshev sign alternation in the Hecke
algebra, but this is stated, not proved.

**What is needed**: A proof that the GS NF term count $\gamma(Z)$ has
the observed gap structure, deriving the magic numbers from the Hecke
algebra without empirical input.

---

### G-9: Neutron–Proton Mass Splitting 0.63% Residual

**Location**: `prop:neutron-proton-splitting`

**The gap**: The prediction $\Delta m = m_\mathfrak{n} - m_\mathfrak{p} \approx 1.302$ MeV
vs CODATA 1.293 MeV has a 0.63% residual.  This is the dilogarithm
volume difference weighted by $\alpha = m_e \cdot 8G$.

This residual is larger than the 0.008% deuterium binding precision.
It likely reflects:
1. The brane tower correction (single-level formula is used; tower adds ~1%)
2. The isospin-breaking from QED (electromagnetic corrections to quark masses)

Neither correction is currently derived in the framework.

---

### G-10: QED Correction in Deuterium Binding

**Location**: `prop:deuterium-derived-binding`

**The gap**: The QED correction $B_\mathrm{phys} = B_\mathrm{strong} \times (1 - \alpha_\mathrm{EM}/2)$
uses the one-loop vacuum polarization formula from standard QED.  The
specific form (factor of $\frac{1}{2}$ from "single charged pair")
is borrowed from textbook QED, not derived from the categorical framework.

**What is needed**: Either (a) derive the QED correction from the
Chern–Simons correction to the categorical action, or (b) cite the
borrowed formula explicitly and flag it as external.

---

### G-11: Energy Scale Residual 0.75%

**Location**: `def:beta-decay-energy-scale`

**The gap**: The categorical energy scale $E_0 = m_e/(q_0(q_0-1)) = 4.186$ MeV
and the CODATA-calibrated value $E_0^\mathrm{cal} = Q_\beta/|\Delta\mathrm{net}| = 4.155$ MeV
disagree by 0.75%.  This is acknowledged as a "brane tower correction"
but not resolved.

Concretely: the free neutron beta decay satisfies
$Q_\beta = 0.78233$ MeV $= E_0 \times 0.18829$, but $E_0^\mathrm{derived}$
misses the CODATA value by 0.75%.

**What is needed**: Show that the tower correction exactly accounts for
the 0.75% gap (i.e. the full tower value of $E_0$ equals 4.155 MeV).

---

### G-12: Crossing-Graded Mass Expansion Conjectural

**Location**: `conj:crossing-graded-mass-expansion`

**The gap**: The mass expansion:

$$
  \mathfrak{m}(\mathcal{K}; q)
  = \sum_{n=0}^{c(\mathcal{K})} \xi(q)^n \cdot \mathfrak{m}^{(n)}_\mathrm{GB}(\mathcal{K})
$$

is explicitly labeled a conjecture because:
1. Lifted-crossing locality hypothesis (`conj:lifted-crossing-locality`) is unproved.
2. The $\xi(q)$ parameter uses the Bloch–Wigner dilogarithm at the
   Descartes shape $z_q$ — the connection between $z_q$ and the
   substrate $q_0$ is assumed, not derived.
3. Convergence of the series for $|\xi| < 1$ requires a uniform bound
   on the brane tower tail.

---

### G-13: JSJ Decomposition Compatibility Not Proved in General

**Location**: `conj:mass-volume-factorization` (§"Why this is a conjecture")

**The gap**: The JSJ decomposition of the atomic link complement is
**verified computationally per atom** but not proved to be canonical
in general (independent of braid representative or reduction path).

---

## Part C — Derivation Chain Completeness Summary

| Step | Status | Gap |
|:-----|:------:|:----|
| A.1 Categorical action | ✓ | — |
| A.2 Frobenius pairing | ✓ | — |
| A.3 Non-abelian Stokes / flat KZ | ✓ | — |
| A.4 Tannaka–Krein → SU_q(2) | ✓ | — |
| A.5 Braid → Hecke algebra | ✓ | — |
| A.6 Descartes condition → q | ⚠ EMPIRICAL + ⚠ CONJECTURAL | G-1 |
| A.7 Confinement LP → B₃ | ✓ (numerical LP) | — |
| A.8 Nucleon quark → braid word | ✓ | — |
| A.9 Nuclear braid word | ✓ | — |
| A.10 Transfer matrix / jet expansion | ✓ | — |
| A.11 GS energy functional | ✓ | — |
| A.12 Wedderburn decomposition | ✓ | — |
| A.13 Atomic mass (zero-param) | ✓ | G-2 (fitted variant) |
| A.14 Binding energy tower | ✓ (formula) | G-3 (accuracy) |
| A.15 Beta decay Q-value | ✓ | G-11 (energy scale) |
| A.16 Beta decay half-life | ❌ MISSING | G-4, G-5 |

---

## Part D — Step-by-Step Derivation Needed to Fill Gaps

### D.1  Volume Conjecture at Real q (closes G-1)

**What to derive**: Show that in the QOU framework, the categorical density
$\rho_q = 1/\hbar_q^2$ is the unique density such that:
$$
  \mathfrak{m}(\varrho) = \mathrm{Vol}(\bar\beta) / \hbar_q^2
$$
for all knot/link representatives $\bar\beta$ (closures of braids).

**Proposed derivation**:
1. Start from the QOU action $\mathcal{S}(\Phi) = \mathrm{tr}(\Phi)$.
2. Under the Hecke quotient, $\mathrm{tr}(\Phi) = \mathrm{tr}_M(\beta)$
   (Markov trace).
3. At the archimedean place ($q \in \mathbb{R}_{>1}$), the Markov trace
   specializes to the Kashaev invariant via the substitution $q \to e^{h}$,
   $h \to 0^+$ following the Habiro–Ohtsuki expansion.
4. The Kashaev invariant satisfies $\log|J_N(K)| \sim \mathrm{Vol}(K) \cdot N/(2\pi)$
   (volume conjecture).  At $q$ real and fixed, this becomes a statement
   about the *pole structure* of the Habiro power series at $q = e^{2\pi i/N}$
   and the analytic continuation.
5. **Key step** (currently conjectural): the Habiro power series
   $\hat{J}(K) \in \mathbb{Z}[[q-1]]$ satisfies a functional equation
   at $q \in \mathbb{R}_{>1}$ that relates $|\hat{J}(K;q)|$ to $e^{\mathrm{Vol}(K)/\hbar_q^2}$.

This step is essentially the open Volume Conjecture.  The paper should
explicitly state this as an adopted axiom or tagged conjecture, and
note that it is the *only* unproved ingredient in the mass formula.

### D.2  Derive β₃ from Brane Dressing (closes G-2)

The fitted $\beta_3 \approx 0.050$ is described as a "$\mathcal{B}_3$
dressing" and "ordering effect in heavy nuclei."  To derive it:

1. Compute the first-order correction to the Wedderburn mass from
   the **brane tower** at level 1: $\sum_i \ln|\Phi_q(\hat{V}_i^\mathrm{full})|$
   vs $\sum_i \ln|\hat{V}_i^\mathrm{full}|$.
2. Show that for large $A$, the tower correction systematically shifts
   the sym/alt channel ratio by a factor $\beta_3$.
3. Verify: $\beta_3 = \ln(\mathrm{Li}_2(q^{-2})) / (Z_\mathrm{ref} \cdot m_e)$
   where $Z_\mathrm{ref}$ is a characteristic nuclear charge scale.

If this derivation succeeds, $\beta_3$ becomes a derived quantity and
the mass formula is truly zero-parameter.

### D.3  Reconcile Binding Energy Formulas (closes G-3)

The tower binding formula (`prop:tower-binding-energy`) and the direct
deuterium formula (`prop:deuterium-derived-binding`) should be the same
computation at $A = 2$.  The discrepancy (4.92 vs 2.22 MeV for D) must
be resolved:

1. Check whether `prop:tower-binding-energy` uses the correct Wedderburn
   weights for $n = 2$ (the deuteron is in $H_2(q)$, not $H_3(q)$).
2. Verify that the $\Phi_q$ tower at $A = 2$ evaluates to the same
   result as the direct $\mathrm{tr}_M(T_{pn} \cdot \mathfrak{n})$ formula.
3. If not: the tower formula is incorrect for small $A$ and needs a
   finite-size correction.

### D.4  Half-Life Derivation from Categorical Framework (closes G-4, G-5)

**Chain of derivation needed**:

1. **Fermi constant**: The categorical coupling $\alpha_\mathrm{EM}$
   from the CS correction gives $\alpha \approx 1/137$.  The weak
   coupling should emerge from the same framework:
   $$
     G_F \cdot m_e^2 = f(q, [n]_q, \ldots)
   $$
   Candidate: $G_F = m_e / (q \cdot [M_W]_q)$ where $[M_W]_q$ is a
   q-integer combination giving the W-boson crossing energy.

2. **Phase-space factor $Q^5$**: The Q-value is derived.  The $Q^5$
   phase-space factor is a kinematic consequence (no free parameters).

3. **Fermi function $f(Z, Q)$**: The Coulomb correction at the nucleus
   can be expressed as the electrostatic interaction of the emitted
   electron with $Z$ proton crossings — this is within the transfer
   matrix framework.

4. **Nuclear matrix element**: $|\mathcal{M}|^2 = |\mathrm{tr}_M(\mathcal{N}_\mathrm{par} - \mathcal{N}_\mathrm{dau})|^2$
   is already defined; needs to be connected to the Gamow–Teller vs.
   Fermi contributions.

### D.5  General Frobenius Packing Density Proof (closes G-6)

**What to prove**: For any atomic link $\mathcal{K}$ in $H_{3A}(q)$,
the alt Wedderburn block $\lambda = (1^3)$ is activated in the Frobenius
pairing if and only if the link is three-body (or higher) entangled.

**Proposed approach**:
1. Express the alt-block activation as a representation-theoretic
   condition: $\mathrm{pr}_\mathrm{alt}(\mathcal{K}) \neq 0$.
2. Show that for a two-component link, the braid word lies in the
   subalgebra $H_2(q) \subset H_3(q)$ at each generator, which contains
   no alt-block contribution ($\chi_\mathrm{alt}$ vanishes on $H_2$).
3. Show that Borromean-type (three-body) entanglement forces the braid
   word out of $H_2 \times H_2$ and into the full $H_3$, activating the alt block.

### D.6  Magic Numbers from Hecke (closes G-8)

**What to prove**: The GS NF growth rate $\gamma(Z)$ has a gap
$\gamma(Z) \notin (1.4, 3.0)$ for all $Z$, with $\gamma(Z) = 1$ exactly
at $Z \in \{2, 8, 20, 28, 50, 82, 126\}$ (magic numbers).

**Proposed approach**:
1. Express $\gamma(Z)$ as a function of the Chebyshev sign factor $c_Z$
   in the NF expansion.
2. The condition $\gamma(Z) = 1$ (exact pairing) becomes a condition on
   $c_Z = 0$, i.e. $q^{-Z} = (-1)^Z q^Z$, i.e. $q^{2Z} = (-1)^Z$.
3. For real $q > 1$: this has no solution with $q^{2Z} > 0$ for odd $Z$.
   For even $Z$: $q^{2Z} = 1$ which is impossible.
4. The magic numbers must emerge from a **different** condition —
   possibly the torus knot $T_{2,m}$ coherence closing condition
   (which closes at $m \in \{2, 8, 20, 28, \ldots\}$ by the Garside
   element periodicity).
5. **Gap**: The identification of magic numbers with torus knot closure
   conditions is stated but the exact periodicity calculation is absent.

---

## Part E — Summary of Computational Backing

| Quantity | Predicted | CODATA/AME | Error | Status |
|:---------|:---------:|:----------:|:-----:|:------:|
| $m_\mathfrak{p}$ (proton mass) | 938.910 MeV | 938.783 MeV | 0.014% | ⚠ G-1 |
| $m_\mathfrak{n}$ (neutron mass) | from NF ordering | 939.565 MeV | 0.001% | ⚠ G-1 |
| $\Delta m_\mathfrak{n} - m_\mathfrak{p}$ | 1.302 MeV | 1.293 MeV | 0.63% | ⚠ G-9 |
| $B({}^2\mathrm{H})$ deuteron binding | 2.2248 MeV | 2.2246 MeV | 0.008% | ✓ |
| $B({}^2\mathrm{H})$ tower formula | 4.92 MeV | 2.22 MeV | 121% | ❌ G-3 |
| $B({}^4\mathrm{He})$ binding | 19.41 MeV | 28.30 MeV | −31% | ❌ G-3 |
| Atomic mass (Z=1–20, zero-param) | — | — | 0.146% MAE | ✓ |
| Atomic mass (Z=1–20, one fitted β₃) | — | — | 0.074% MAE | ⚠ G-2 |
| $Q_\beta$ (free neutron decay) | 0.782 MeV | 0.782 MeV | 0.75%* | ⚠ G-11 |
| $T_{1/2}$ (any beta decay) | NOT DERIVED | — | — | ❌ G-4 |
| $\alpha_\mathrm{EM}$ | $\approx 1/137.0$ | 1/137.036 | 0.026% | ✓ |

*Scale residual, not Q-value error.

---

## Part F — Prioritized Gap Resolution

### Priority 1 (Critical for logical consistency)
- **G-1** Volume conjecture at real $q$: adopt as explicit conjecture/axiom.
- **G-4/G-5** Half-life: scope explicitly or begin derivation of $G_F$.
- **G-3** Reconcile binding energy formulas for $A = 2, 4$.

### Priority 2 (For mass formula completeness)
- **G-2** Derive or bound $\beta_3$ from tower correction.
- **G-9** Derive n–p splitting residual from tower/isospin corrections.
- **G-11** Verify energy scale $E_0$ residual from tower.

### Priority 3 (For general nuclear physics)
- **G-6** Prove Frobenius packing density rule.
- **G-8** Prove magic numbers from Hecke/torus knot periodicity.
- **G-10** Derive QED correction from categorical Chern–Simons action.
- **G-12** Prove crossing-graded expansion convergence.
- **G-13** Prove JSJ decomposition canonicity.

---

## Appendix: Conjectures Underpinning Physical Computations

| Conjecture | Used in | Status |
|:-----------|:--------|:------:|
| `conj:mass-volume-factorization` | ALL mass predictions | Unproven |
| `conj:crossing-graded-mass-expansion` | Heavy nucleus masses | Unproven |
| `conj:lifted-crossing-locality` | Mass expansion | Unproven |
| `conj:shell-closure-nf-term-count` | Pairing term, magic numbers | Comp. verified |
| `conj:palindromicity-orbital-type` | Shell correction | Comp. verified |
| `conj:periodic-table-demand` | Stability band | Comp. verified |
| Volume conjecture at real $q$ | Particle masses | Open (classical conj. unproven) |

---

*This audit was prepared on branch `copilot/audit-mass-and-beta-decay`.
Each flagged gap corresponds to a potential new content block, lemma,
or explicit conjecture declaration in the paper.*
