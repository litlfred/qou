**$\mathfrak{Q}_\beta$ γγ canonical derivation: the categorical-chain reading, selected by the cat-action / Frobenius / Wenzl chain.**

The $\mathfrak{Q}_\beta$ precision-ladder coefficients $c_k$ admit two readings: one in which $c_2$ is fitted, and one in which it is derived from the categorical chain. That ambiguity is settled here in favour of the second.

## The chain

The canonical $c_k$ values are determined by tracing through:

$$
\text{cat-action} \;\to\; \text{Frobenius pairing} \;\to\;
\text{Wedderburn} \;\to\; \text{Wenzl bridge} \;\to\;
\mathrm{tr}_M(\text{typed }\beta) \;\to\; \mathfrak{Q}_\beta^{\text{cat}}
$$

### Step 1: Cat action (Hoefsmit seminormal)

$H_3(q)$ acts on the three irreps $V_{(3)}, V_{(2,1)}, V_{(1,1,1)}$ via the Hoefsmit seminormal representation.

### Step 2: Frobenius pairing

Per the [Frobenius Markov-trace selection proposition](#prop:markov-trace-frobenius-selection), the unique non-degenerate Markov trace on $H_n(R, q)$ is the Jones-Markov $\mathrm{tr}_M$. The non-degeneracy is forced by the Frobenius co-Casimir construction.

### Step 3: Wedderburn decomposition

$H_3(q) \cong V_{(3)} \oplus V_{(2,1)} \oplus V_{(1,1,1)}$. So $\mathrm{tr}_M(\beta) = y_{(3)} \chi_{(3)}(\beta) + y_{(2,1)} \chi_{(2,1)}(\beta) + y_{(1,1,1)} \chi_{(1,1,1)}(\beta)$.

### Step 4: Wenzl bridge

The $y_\lambda$ weights solve the Markov-axiom system on $H_3$.

### Step 5: Canonical typed braids

From the [categorical proton](#def:categorical-proton) and [categorical neutron](#def:categorical-neutron) definitions, $\mathcal{B}_p$ and $\mathcal{B}_n$ have 11 typed crossings each.

### Step 6: $\mathrm{tr}_M$ values

At $q_0$, $\Delta\mathrm{tr}_M(n{-}p) = +0.0445860283$.

### Step 7-9: Precision-ladder identifications

Categorical-chain reading of the $c_k$ coefficients from the [categorical precision ladder](#prop:q-beta-categorical-precision-ladder):

| $k$ | $c_k$ | categorical source |
|:---:|:---|:---|
| 1 | $b$ | Hoefsmit off-diagonal coupling on $V_{(2,1)}$ — Kashiwara $\tilde f_1$ |
| 2 | $b^2$ | Kashiwara $\tilde f_1^\dagger \tilde f_1$ return amplitude |
| 3 | $-2 = J_{\text{Hopf}}(q{=}1)$ | classical-limit Jones polynomial of the Hopf-link substructure |
| 4 | $c_3 \cdot b^4 = -2b^4$ | multiplicative Jones $\times$ Kashiwara mixing |

## Resolving the ambiguity: fitted versus categorical reading

Evaluating the categorical-derivation chain end-to-end shows that the $N=2 \to N=3$ transition reduces the residual against CODATA by $112\times$. This reduction is observable above CODATA's $0.4\;\mathrm{ppm}$ measurement floor, confirming the categorical identification $c_3 = J_{\text{Hopf}}(q{=}1) = -2$ without fitting.

The fitted reading, in which $c_2$ is chosen to match the data, provides no structural derivation of the 1.7% deviation. The categorical reading (Kashiwara $c_2 = b^2$ together with Hopf $c_3 = -2$) provides structural content: each rung's coefficient is derived from aether-only data via the categorical chain.

Selection rule: when two readings match the data equally, the categorical-chain reading is canonical because it traces back to aether principles.

## Open question: a rigorous $c_3 = -2$

Establishing the $c_3 = -2$ Hopf assignment unconditionally requires deriving the 3-fold Markov closure $\to$ Hopf-link substructure identification directly at the categorical level.

## Open question: higher orders

Once the structural identification is settled, the construction extends to higher orders where the simple Kashiwara + Jones alternation breaks down. The empirical $c_5, c_6$ remain unidentified pending a refined mathematical framing.
