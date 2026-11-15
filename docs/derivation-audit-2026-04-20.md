# Step-by-Step Derivation of 𝔪(ρ) and B(Z,N) from the Categorical Action

*Compiled 2026-04-20 by traversing all content blocks in the derivation chain.*

## Part I — Categorical Action → Mass Identity

### Step 1 — Categorical action
- **Block**: `def:categorical-action` — `folio/quantum-observable-universe/quantum-observable-universes/categorical-action.md`
- **Given**: QOU $(\mathbf{C}, A, \tau)$ with Frobenius–Hopf $A$, rigid monoidal structure (ev, coev), endomorphism $\Phi \in \text{End}_\mathbf{C}(A)$.
- **Equation**: $\mathcal{S} = \text{ev}_A \circ (\text{id}_{A^\vee} \otimes \Phi) \circ \text{coev}_A = \text{tr}(\Phi)$

### Step 2 — Mass identity
- **Block**: `def:mass-identity`
- **Given**: Closed cycle $\varrho: \mathbf{1} \to A$, comult $\Delta$, Frobenius form $\int_A$, trace tr, Frobenius norm $\|\cdot\|$.
- **Equation**: $\mathfrak{m}(\varrho) = \|\text{tr}((\int_A \otimes \text{id}) \circ \Delta \circ \varrho)\|$

### Step 3 — Frobenius pairing
- **Block**: `def:frobenius-pairing`
- **Equation**: $\langle \cdot, \cdot \rangle_F = \int_A \circ \mu$, induces $A \cong A^\vee$.

## Part II — Descent to Hecke Algebra

### Step 4 — Hecke mass element
- **Block**: `def:hecke-mass-element` — braids-and-knots/
- **Given**: Braid $\beta \in B_n$, fibre functor $\tau$, descent involution $\hat\tau_n$, mass integrand $\alpha_\varrho$.
- **Equation**: $\Phi_{\text{mass}}(\beta) = \tau(L_{\alpha_\varrho}) \in H_n(q) = \Phi^{\text{desc}}(\beta) + \Phi^{\text{trans}}(\beta)$

### Step 5 — Jones–Markov trace (external)
- **Block**: `thm:jones-markov-trace`
- **Equation**: Unique linear $\text{tr}_M: H_n(q) \to \mathbb{C}$ with normalisation, cyclicity, and Markov axiom $\text{tr}_M(xT_n^{\pm1}) = z^{\pm1} \text{tr}_M(x)$ where $z = (q-1)/(q^{1/2}+q^{-1/2})^2$.

### Step 6 — Mass via Markov trace
- **Block**: `prop:hecke-mass-trace`
- **Equation**: $\mathfrak{m}(\varrho_\beta) = |\text{tr}_M(\Phi_{\text{mass}}(\beta))|$
- Decomposes as $\text{tr}_M(\Phi^{\text{desc}}) + \sum_i \text{tr}_M(\Phi^{\text{trans}}_i)$.

## Part III — Single-Level Mass

### Step 7 — Categorical mass as Markov trace
- **Block**: `prop:categorical-mass-markov`
- **Scope**: single brane level only (base); Nakayama $\Psi = S^2 = \text{id}$ in $H_n(q)$.
- **Equation**: $\mathfrak{m}(\varrho)|_\text{single} = |\text{tr}_M(\rho(\beta))|$

## Part IV — Topological (Brane Tower) Decomposition

### Step 8 — Topological mass theorem
- **Block**: `thm:topological-mass`
- **Given**: Tower $\{A_n\}$, descent splitting $\text{End}(A_{n+1}) = \mathcal{A}^{\text{desc}} \oplus \mathcal{A}^{\text{trans}}$; descent = image of $\hat\tau_n$ = copy of level-$n$ base; transient = kernel (new modes).
- **Equation**: $\mathfrak{m}(\varrho) = \|\text{tr}_{\text{desc}}(\varrho)\| + \sum_i \|\text{tr}_{\text{trans}}(\varrho, p_i)\|$

### Step 9 — Topological mass formula (archimedean)
- **Block**: `prop:topological-mass-formula`
- **Equation**: $\mathfrak{m}(K) = \text{Vol}(K)/\hbar_q^2$ with $\hbar_q = 1 - 1/q$.

## Part V — Jet Tower Mass

### Step 10 — Mass endomorphism tower (the explicit computational formula)
- **Block**: `prop:mass-endomorphism-tower` — braids-and-knots/mass-endomorphism-tower.md
- **Equation** (verbatim):
$$\mathfrak{m}(\varrho) = \Bigl|\prod_{i=0}^{n-2} \hat{V}_i^\text{full}\Bigr| + \sum_{i=0}^{n-2} \Phi_q(|\hat{V}_i^\text{full}|) + z^2 \sum_{i<j,\ (i,j) \in \mathcal{P}} \Phi_q(|\hat{V}_i^\text{full} \hat{V}_j^\text{full}|)$$
- **Inputs**: $\Phi_q(x) = \prod_{k\geq1}(1-q^{-k}x)^{-1}$, $z = 1/(q^{1/2}+q^{-1/2})$, $\hat{V}_i^\text{full}$ = additive Wedderburn traced volume at generator $i$.

### Step 11 — Jet-brane reformulation (per-level tower with pentagon ascension)
- **Block**: `rem:mass-endomorphism-jet-tower` (recently edited: pentagon ascension + single-descended-term)
- **Equation**:
$$\mathfrak{m}(\varrho) = \underbrace{\bigl|\prod_i \hat{V}_i^{(0)}\bigr|}_\text{descended, level 0 only} + \sum_{n=0}^N \Bigl(\sum_i \Phi_q(|\hat{V}_i^{(n)}|) + z^2 \sum_{(i,j) \in \mathcal{P}_n} \Phi_q(|\hat{V}_i^{(n)} \hat{V}_j^{(n)}|)\Bigr)$$
- **Pentagon ascension**: triples at level $n$ rewrite as pairs/singletons at level $n+1$ via $\Phi_q(v)\Phi_q(u) = \Phi_q(u)\Phi_q(uv)\Phi_q(v)$ when $uv = q\,vu$.
- **$\mathcal{P}_n$ resolved**: now **all pairs $i<j$** via `thm:markov-trace-factorization` (two successive Markov peels give $\text{tr}_M(\sigma_i \sigma_j) = z^2$ for every distance).
- **Open subconjectures remaining**:
  1. **Jet-level convergence tail bound**: conditional on $|\Delta^{(n)}| \leq \Delta_\text{max}$ (geometric-series bound); uniform $\Delta_\text{max}$ proof still open.
  2. **Pentagon uv-commutation**: verification of $uv = q\,vu$ at traced-volume level not written out.
  3. **Descent of pairs under $\hat\tau_n$** (sharpness of ascension bound).

## Part VI — Atomic Mass (Wedderburn Decomposition)

### Step 12 — Three-invariant / three-Wedderburn-block formula
- **Block**: `thm:wedderburn-mass-formula`
- Three blocks: sym (+q), std (2×2), alt (−q⁻¹). Weights $w_\text{sym}, w_\text{std}, w_\text{alt}$ at $n=3$: $\approx 0.165, 0.669, 0.165$.
- **Equation**: $\hat{V}_i^\text{full} = w_\text{sym} \lambda_i^\text{sym} + w_\text{std} \hat{V}_i^\text{std} + w_\text{alt} \lambda_i^\text{alt}$.
- Atomic mass: $\mathcal{M}(Z,N) = Z m_p + N m_n + Z m_e + \alpha \sum_i \ln|\hat{V}_i^\text{full}|$ with binding scale $\alpha = m_e \cdot 8G$ (Catalan's constant × 8).

## Part VII — Binding Energy

### Step 13 — Tower binding formula
- **Block**: `prop:tower-binding-energy`
- **Equation**: $B(Z,N) = \sum_{\lambda \in \{\text{sym,std,alt}\}} w_\lambda \cdot m_e \cdot \sum_i \ln|\Phi_q(\hat{V}_i^\lambda)|$
- $M(Z,N) = Z m_p + N m_n + Z m_e - B(Z,N)$

### Step 14 — Deuterium closed-form (validation)
- **Block**: `prop:deuterium-derived-binding`
- **Equation**: $B_\text{strong} = [\text{tr}_M(\mathfrak{p}) + \text{tr}_M(\mathfrak{n}) - \text{tr}_M(T_{pn} \mathfrak{n})] \cdot m_e \cdot 8G$, with QED correction $B = B_\text{strong}(1 - \alpha_\text{EM}/2)$.
- Result: 2.2248 MeV vs AME 2.2246 MeV (**0.008% error**).

## Ingredients

- **Constants**: $q_0 = 1.10998$, $\hbar_q = 0.0998$, $z = 0.49932$, $H_A = q - q^{-1} = 0.20906$
- **Physical**: $m_e = 0.5110$ MeV (CODATA), $m_p = :val[m_p_MeV]{precision=6}$, $m_n = :val[m_n_MeV]{precision=6}$, Catalan $G = 0.9160$, $\alpha = m_e \cdot 8G = 3.7445$ MeV
- **Weights at n=3**: $w_\text{sym} = w_\text{alt} = 1/[3]_q! \approx 0.165$, $w_\text{std} = [2]_q^2/[3]_q! \approx 0.669$
- **Algebras**: rigid monoidal $\mathbf{C}$, Frobenius-Hopf $A$, fibre functor $\tau$, Hecke $H_n(q)$
- **Tower**: $A_{n+1} = A_n \otimes \Omega^1(A_n)$ with descent involution $\hat\tau_n$

## Explicit mass-tower formula (verbatim from paper)

$$\mathfrak{m}(\varrho) = \Bigl|\prod_{i=0}^{n-2} \hat{V}_i^\text{full}\Bigr| + \sum_{i=0}^{n-2} \Phi_q(|\hat{V}_i^\text{full}|) + z^2 \sum_{\substack{i < j\\(i,j) \in \mathcal{P}_n}} \Phi_q(|\hat{V}_i^\text{full} \hat{V}_j^\text{full}|)$$

Single brane level formula; at the jet level, descended term keeps **level 0 only**; singletons + pairs appear **per level** and are summed over $n = 0, \ldots, N$ (quadratic truncation justified by pentagon ascension).

## Gaps

1. **Mass endomorphism conjecture** (`conj:mass-endomorphism`): closed form $\Phi_\text{mass}$ as a single $H_n(q)$ element — open.
2. **$\mathcal{P}_n$ = all-pairs** proven in updated `rem:mass-endomorphism-jet-tower` via `thm:markov-trace-factorization`. Previous adjacency restriction removed.
3. **Jet-level convergence tail bound**: conditional; uniform $|\Delta^{(n)}| \leq \Delta_\text{max}$ proof pending.
4. **Pentagon $uv = q\,vu$ check** on traced volumes: expected but unwritten.
5. **Descent sharpness** on pairs: pentagon gives upper bound; exact sharpness open.
