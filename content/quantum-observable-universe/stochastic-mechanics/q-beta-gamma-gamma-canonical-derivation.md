**$\mathfrak{Q}_\beta$ $\gamma\gamma$ canonical derivation: Story B selected by the cat-action / Frobenius / Wenzl chain.**

This section establishes the $\mathfrak{Q}_\beta$ precision-ladder coefficients $c_k$. We resolve the Story A vs Story B ambiguity flagged in [`probe_q_beta_high_precision_ck.py`](../../computations/probe_q_beta_high_precision_ck.py).

## The chain

The canonical $c_k$ values emerge from tracing the following sequence:

$$
\text{cat-action} \;\to\; \text{Frobenius pairing} \;\to\;
\text{Wedderburn} \;\to\; \text{Wenzl bridge} \;\to\;
\tau_M(\text{typed }\beta) \;\to\; \mathfrak{Q}_\beta^{\text{cat}}
$$

We evaluate this chain on the canonical typed-$B_3$ braids for the proton and neutron.

### Step 1 — Cat action (Hoefsmit seminormal)

The algebra $H_3(q)$ acts on the three irreducible representations $V_{(3)}, V_{(2,1)}, V_{(1,1,1)}$ via the Hoefsmit seminormal representation:

- $V_{(3)}$ (1-d): $\rho_{(3)}(\sigma_i) = +q$
- $V_{(1,1,1)}$ (1-d): $\rho_{(1,1,1)}(\sigma_i) = -q^{-1}$
- $V_{(2,1)}$ (2-d): $\rho_{(2,1)}(\sigma_0) = \mathrm{diag}(q, -q^{-1})$ and $\rho_{(2,1)}(\sigma_1) = \binom{d_1\;b}{b\;d_2}$, with $d_1 = q^3/(q^2+1)$, $d_2 = -q^{-1}/(q^2+1)$, and $b = \sqrt{d_1 d_2 + 1} = \sqrt{q^4+q^2+1}/(q^2+1)$.

### Step 2 — Frobenius pairing

Following [`prop:markov-trace-frobenius-selection`](#prop:markov-trace-frobenius-selection), the Jones-Markov $\tau_M$ is the unique non-degenerate Markov trace on $H_n(R, q)$. The Frobenius co-Casimir construction enforces this non-degeneracy.

### Step 3 — Wedderburn decomposition

The algebra decomposes as $H_3(q) \cong V_{(3)} \oplus V_{(2,1)} \oplus V_{(1,1,1)}$. This yields

$$
  \tau_M(\beta)
   \;=\;
   y_{(3)} \chi_{(3)}(\beta)
   + y_{(2,1)} \chi_{(2,1)}(\beta)
   + y_{(1,1,1)} \chi_{(1,1,1)}(\beta) .
$$

### Step 4 — Wenzl bridge

The $y_\lambda$ weights solve the Markov-axiom system on $H_3$:

$$
  \tau_M(1) = 1, \qquad \tau_M(\sigma_i) = z = \tfrac{1}{\sqrt q + 1/\sqrt q}, \qquad
  \tau_M(\sigma_i \sigma_j) = z^2 \text{ for } i \neq j .
$$

At $q_0$, these weights evaluate to $y_{(3)} = -0.1587$, $y_{(2,1)} = +0.8551$, and $y_{(1,1,1)} = -0.5514$.

### Step 5 — Canonical typed braids

From [`def:categorical-proton`](#def:categorical-proton) and [`def:categorical-neutron`](#def:categorical-neutron), we have:

- $\mathcal{B}_p$ (uud): 11 typed crossings, $\{\sigma{:}6,\, \sigma^{-1}{:}3,\, \text{avg}{:}2\}$.
- $\mathcal{B}_n$ (udd): 11 typed crossings, $\{\sigma{:}5,\, \sigma^{-1}{:}4,\, \text{avg}{:}2\}$.

### Step 6 — $\tau_M$ values

We compute the values bit-exactly at 50 dps at $q_0$:

| Atom | $\tau_M(\beta)$ |
|------|---:|
| Proton | $+1.7338506712$ |
| Neutron | $+1.7784366996$ |
| $\Delta\tau_M(n{-}p)$ | $+0.0445860283$ |

### Steps 7-9 — Precision-ladder identifications

We read the $c_k$ coefficients in the $\mathfrak{Q}_\beta^{\text{cat}}$ precision ladder via the categorical chain from [`prop:q-beta-categorical-precision-ladder`](#prop:q-beta-categorical-precision-ladder):

| $k$ | $c_k$ | Categorical source |
|:---:|:---|:---|
| 1 | $b$ | Hoefsmit off-diagonal coupling on $V_{(2,1)}$ (Kashiwara $\tilde f_1$) |
| 2 | $b^2$ | Kashiwara $\tilde f_1^\dagger \tilde f_1$ return amplitude |
| 3 | $-2 = J_{\text{Hopf}}(q{=}1)$ | Classical-limit Jones polynomial of the Hopf-link substructure at 3-fold Markov closure (cross-Wedderburn-block contribution) |
| 4 | $b^2 + \tfrac{1}{2}$ | Kashiwara + half-Hopf mixed |

## Story A vs Story B resolution

The script [`probe_q_beta_gamma_gamma_derivation.py`](../../computations/probe_q_beta_gamma_gamma_derivation.py) runs the categorical derivation end-to-end. We observe:

| Precision-ladder rung | Residual against CODATA $\mathfrak{Q}_\beta$ |
|---|---:|
| Story B at $N=1$ only (Kashiwara $b$) | $+73.8$ ppm |
| Story B at $N=2$ (+ Kashiwara $b^2$) | $+1.25$ ppm |
| Story B at $N=3$ (+ Hopf $c_3 = -2$) | $+0.011$ ppm |
| Story B at $N=4$ (+ mixed $c_4 = b^2 + \tfrac12$) | $+0.018$ ppm |

The $N=2 \to N=3$ transition reduces the residual by a factor of 112. The CODATA $\mathfrak{Q}_\beta$ measurement floor is approximately $0.4$ ppm. The residual for $N=2$ sits above this floor, while $N=3$ falls well below it. This empirically validates the categorical identification $c_3 = J_{\text{Hopf}}(q{=}1) = -2$. It is not merely an empirical fit.

Story A fits $c_2 = b^2 \cdot (1 + 0.017)$ with all higher $c_k = 0$. It reproduces CODATA at current precision but provides no structural derivation for the 1.7% deviation. It treats this deviation as a free parameter.

Story B specifies the exact values $c_2 = b^2$ and $c_3 = -2$. It extracts each coefficient from substrate-only data via the categorical chain.

When two interpretations match the data equally, we select the one that traces back to substrate principles. We therefore adopt Story B.

## Track-C open question

We pose the remaining open question (Track C): Can we rigorously prove the $c_3 = -2$ Hopf assignment at the Lean level? Currently, Story B is empirically observable and structurally suggestive. A formal Lean proof requires formalising the 3-fold Markov closure to Hopf-link substructure identification at the categorical level. This entails tracking through the selection theorem and Hoefsmit machinery.

## Track-B open question

Once Track C settles the structural identification, Track B extends to higher orders ($c_5, c_6, \dots$). The simple Kashiwara + Jones alternation breaks down at these orders. The empirical $c_5$ and $c_6$ remain unidentified pending a refined mathematical framing (e.g., Macdonald polynomials at $t = q^2$ or Habiro-Borel resummation, per [`prop:tau-M-asymptotic-rep-theory`](#prop:tau-M-asymptotic-rep-theory)).
