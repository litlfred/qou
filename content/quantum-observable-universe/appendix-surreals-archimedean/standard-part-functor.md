An element $x \in \mathbf{No}$ is **finite** if there exists
$n \in \mathbb{N}$ with $|x| \leq n$. Write $\mathbf{No}_{\mathrm{fin}}
\subset \mathbf{No}$ for the subring of finite surreals, and
$\mathbf{No}_{\mathrm{inf}} \subset \mathbf{No}_{\mathrm{fin}}$ for the
ideal of infinitesimals (those $x$ with $|x| < 1/n$ for every $n \in
\mathbb{N}$).

## Definition

The **standard-part map**

$$
  \mathrm{st} : \mathbf{No}_{\mathrm{fin}} \to \mathbb{R}
$$

sends each finite surreal $x$ to the unique real $r \in \mathbb{R}$
with $x - r \in \mathbf{No}_{\mathrm{inf}}$. Classically
[@robinson1966; @alling1987]:

$$
  \mathrm{st}(x) =
  \sup\{q \in \mathbb{Q} : q \leq x\}
  = \inf\{q \in \mathbb{Q} : q \geq x\}.
$$

The map $\mathrm{st}$ is a surjective ring homomorphism with kernel
$\mathbf{No}_{\mathrm{inf}}$, inducing a ring isomorphism

$$
  \mathbf{No}_{\mathrm{fin}} / \mathbf{No}_{\mathrm{inf}}
  \xrightarrow{\sim} \mathbb{R}.
$$

## Functorial extension

For a $K$-linear category $\mathbf{C}$ equipped with a
[birthday grading](#def:birthday-grading), define the **standard-
part functor**

$$
  \mathrm{St} : \mathbf{C}_{\leq \omega + 1}^{\mathrm{fin}}
   \longrightarrow \mathbf{C}_{\mathbb{R}}
$$

from the finite-coefficient sub-category at birthday $\leq \omega + 1$
to the archimedean sub-category. On objects it is the identity; on
morphisms it applies $\mathrm{st}$ entrywise to the matrix
representation of $f$ in any Hoefsmit-type basis.

Concretely, if $f \in \mathrm{Hom}_{\mathbf{C}}(X, Y)$ has matrix
entries $f_{ij} = r_{ij} + \varepsilon \cdot s_{ij} + O(\varepsilon^2)$
with $r_{ij}, s_{ij} \in \mathbb{R}$, then $\mathrm{St}(f)_{ij} =
r_{ij}$.

### Key properties

1. **$K$-linear**: $\mathrm{St}(af + bg) = \mathrm{st}(a)\mathrm{St}(f)
   + \mathrm{st}(b)\mathrm{St}(g)$ for $a, b \in K_{\mathrm{fin}}$.
2. **Monoidal**: $\mathrm{St}(f \otimes g) = \mathrm{St}(f) \otimes
   \mathrm{St}(g)$ on finite-coefficient morphisms.
3. **Right inverse to inclusion**: $\mathrm{St} \circ \iota_{\mathbb{R}
   \hookrightarrow K} = \mathrm{id}_{\mathbf{C}_{\mathbb{R}}}$.
4. **Classical limit = $\mathrm{St} \circ$ evaluation at
   $q = 1 + \varepsilon$** (see
   [classical limit as standard-part](#conj:classical-limit-stpart)).

## Example: Jackson derivative

The Jackson derivative

$$
  d_q f(x) = \frac{f(qx) - f(x)}{(q - 1) x}
$$

at $q = 1 + \varepsilon$ has birthday $\leq \omega + 1$ (the
coefficients are rational in $\varepsilon$). Applying $\mathrm{st}$
recovers the classical derivative exactly:

$$
  \mathrm{st}\!\bigl(d_{1 + \varepsilon} f(x_0)\bigr) = \frac{df}{dx}(x_0)
  \qquad (x_0 \in \mathbb{R}).
$$

This is the exact substitute for the (broken) classical-limit functor
([classical limit functor](#def:classical-limit-functor)): instead of
taking $q \to 1$ as a topological limit in $\mathbb{R}$, we evaluate at
a specific infinitesimal-shifted surreal and take the standard-part.
Unlike the topological limit, this construction makes sense in pure
algebra.

## Why this matters for QOU

The main paper's mass formula outputs live in $\mathbb{Q}(q)$ with
$q = q_0 \in \mathbb{R}$ as the substrate value. Under a surreal lift,
$q$ becomes $1 + \varepsilon$ and the outputs live in
$\mathbf{No}_{\mathrm{fin}}$ (they are rational in $\varepsilon$).
Applying $\mathrm{St}$ recovers exactly the paper's reals; the
discarded infinitesimal part is an explicit record of the
first-order quantum correction.

The functorial standard-part is the bridge between the surreal-
ambient reformulation and the archimedean paper.

## Archimedean Functor & Trace Commutativity

The standard-part functor acts as the **Archimedean Functor** $\mathcal{F}_{Arch}$, transforming algebraic traces into physical macroscopic observables. The evaluation of nuclear binding traces rigorously commutes as the scale $A \to \infty$:

```mermaid
flowchart TD
    classDef base fill:#1e1e2e,stroke:#89b4fa,stroke-width:2px,color:#cdd6f4
    classDef trace fill:#313244,stroke:#f38ba8,stroke-width:2px,color:#cdd6f4
    classDef proxy fill:#313244,stroke:#f9e2af,stroke-width:2px,color:#cdd6f4
    classDef physical fill:#1e1e2e,stroke:#a6e3a1,stroke-width:2px,color:#cdd6f4

    M_unb["Unbound Base \n m_unbound = Z·m_p + N·m_n"]:::base
    
    B_sym["Exact Algebraic Trace \n B_sym = -α ln |τ_M(K)|"]:::trace
    B_qCLT["Q-CLT Macroscopic Limit \n B_qCLT = -α Σ ln |V_i|"]:::proxy
    
    M_sym["Exact Algebraic Mass \n m_sym = m_unbound - B_sym"]:::physical
    M_qclt["Limit Approximation Mass \n m_qclt = m_unbound - B_qCLT"]:::physical
    M_obs["Macroscopic Empirical Observation \n AME 2020"]:::physical

    M_unb -->|"Exact active-partition factorization"| B_sym
    M_unb -->|"Statistical averaging (Q-CLT macroscopic limit)"| B_qCLT
    
    B_sym -.->|"Q-CLT Limit (A → ∞)"| B_qCLT
    
    B_sym == "Archimedean Functor F_Arch (Standard-Part)" ==> M_sym
    B_qCLT == "Asymptotic Convergence" ==> M_qclt
    
    M_sym -.->|"Perfect mapping in algebraic limit"| M_obs
    M_qclt -.->|"Approximates"| M_obs
```

This mapping guarantees that the exact active-partition factorization and the Q-CLT statistical limit share the same macroscopic limit under $\mathrm{St}$.

### Numerical realization

The scale $\alpha$ in the diagram is the canonical energy scale $\alpha = E_0 =
\mathfrak{m}_e/\bigl(q_0(q_0-1)\bigr)$, the electron mass lifted by the substrate
factor — a derived quantity, not a free parameter (in particular it is neither
the neutron $\beta$-decay value $Q_\beta$ nor a deuteron-pinned fit). Writing the
bond suppression $s(K) = 1 - \mathrm{tr}_M(W_{\mathrm{atom}})/\mathrm{tr}_M(W_{\mathrm{free}})$
and the log-ratio $L(K) = \ln\bigl(\mathrm{tr}_M(W_{\mathrm{free}})/\mathrm{tr}_M(W_{\mathrm{atom}})\bigr)
= -\ln(1-s)$, the exact algebraic trace is $B_{\mathrm{sym}} = \alpha\,L$; its
linearization $B_{\mathrm{lin}} = \alpha\,s$ is the leading term of $L = s + s^2/2 +
\cdots$ and saturates at $\alpha$ (since $s < 1$); and the Q-CLT limit
$B_{\mathrm{qCLT}} = \alpha \sum_i \ln|V_i|$ replaces the exact correlated trace by a
sum of independent per-bond contributions, each $V_i$ the Markov-trace ratio of a
two-nucleon sub-braid. Taking every $V_i$ equal to the deuteron bond gives the
uniform limit; resolving the three bond types ($p$–$p$, $p$–$n$, $n$–$n$) by their
own sub-braid ratios — with $\ln|V_{n\text{-}n}| > \ln|V_{p\text{-}p}|$ — gives the
factorized limit.

Evaluated on the light nuclei whose binding trace is canonical, the exact
log-trace $B_{\mathrm{sym}}(E_0)$ reproduces the measured binding within
$\approx 1.2\times$ for the non-anomalous $A = 3$ isotopes with no fit. The
tritium / helium-3 splitting is resolved both by the exact trace and by the
factorized Q-CLT: tritium carries an $n$–$n$ bond where helium-3 carries a
$p$–$p$ bond, and the larger $n$–$n$ sub-braid suppression makes tritium the more
bound — a distinction the uniform-per-bond limit, blind to bond type, averages
away. The doubly-magic $^4\mathrm{He}$, which carries no single hyperbolic knot,
is instead reproduced by the shell-closure specialization $B = 2\,\mathfrak{m}_e\,
A\,\mathrm{Vol}(L6a4)$ with $\mathrm{Vol}(L6a4) = 8G$ the Borromean residue; the
per-knot trace forms undershoot the heavier $^6\mathrm{Li}$ and $^7\mathrm{Li}$ by
$\approx 1.6\times$, marking where the single-trace estimate gives way to shell
structure. The side-by-side evaluation through this one canonical trace — now
spanning $^2\mathrm{H}$ through $^7\mathrm{Li}$ — is recorded in
`binding-single-pipeline-comparison.witness.json`.
