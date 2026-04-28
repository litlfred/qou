**Proposition (Landauer: Cauchy--Schwarz insufficiency).**

*There exists a semisimple Frobenius algebra
$(A, \mathrm{tr}_A) \in \mathbf{C}$ — in fact an infinite family
parameterised by the number of blocks — such that the L${}^2$-
Cauchy--Schwarz lower bound*

$$
  \tau(f^\dagger f) \;\geq\; \frac{|\tau(f^\dagger C)|^2}{\|C\|^2}
$$

*on the trace of a unit-creation morphism $f \colon \mathbf{1} \to A$
(normalised by $\tau(f^\dagger C) = 1$, where $C = \sum_\lambda
p_\lambda / (d_q(\lambda) \, \tau(p_\lambda))$ is the canonical
creation morphism associated with the Wedderburn decomposition
$A = \bigoplus_\lambda A_\lambda$) is **strictly less** than the
Landauer bound $\tau(C_{\dim_q}) = \sum_\lambda 1/d_q(\lambda)$
conjectured by [`conj:tau-codim-landauer`](#conj:tau-codim-landauer).
Hence no proof of `conj:tau-codim-landauer` can rest on the
L${}^2$-Cauchy--Schwarz inequality alone.*

**Computation of both bounds.**  For a Frobenius algebra
$A = \bigoplus_{\lambda} A_\lambda$ with quantum dimensions
$\{d_q(\lambda)\}$ and idempotent traces
$\{\tau(p_\lambda)\}$, direct calculation in the centre gives:

$$
  \tau(C) \;=\; \sum_\lambda \frac{1}{d_q(\lambda)},
  \qquad
  \|C\|^2 \;=\; \tau(C^\dagger C) \;=\;
  \sum_\lambda \frac{1}{d_q(\lambda)^2 \, \tau(p_\lambda)},
$$

so the Cauchy--Schwarz lower bound under unit creation
normalisation is

$$
  \tau(f^\dagger f) \;\geq\; \frac{1}{\|C\|^2}
  \;=\; \left(\sum_\lambda \frac{1}{d_q(\lambda)^2 \, \tau(p_\lambda)}\right)^{-1}.
$$

**Balanced family witness.**  Take $|\Lambda|$ blocks with
$d_q(\lambda) = \tau(p_\lambda) = 1$ for every $\lambda$.  Then
$\tau(C) = |\Lambda|$ and $\|C\|^2 = |\Lambda|$, so

$$
  \frac{1}{\|C\|^2} \;=\; \frac{1}{|\Lambda|}
  \;<\; |\Lambda| \;=\; \tau(C_{\dim_q})
  \quad\text{whenever } |\Lambda| \geq 2.
$$

The CS-to-Landauer ratio is $1/|\Lambda|^2$, which tends to $0$
as $|\Lambda| \to \infty$.  In particular for the minimal
$|\Lambda| = 2$ witness,

$$
  \frac{1}{\|C\|^2} \;=\; \tfrac{1}{2}
  \quad\text{but}\quad
  \tau(C_{\dim_q}) \;=\; 2,
$$

so any L${}^2$-Cauchy--Schwarz argument can deliver at most
$\tau(f^\dagger f) \geq 1/2$, not the Landauer claim
$\tau(f^\dagger f) \geq 2$.

**Independent computational validation.**  The script
[`tau_codim_conjectures_validate.py`](https://github.com/litlfred/qou/blob/main/folio-assistant/computations/tau_codim_conjectures_validate.py)
records both bounds for the balanced family at
$|\Lambda| \in \{2, 3, 5, 10, 20\}$ in
[`tau-codim-conjectures-validation.witness.json`](https://github.com/litlfred/qou/blob/main/folio-assistant/computations/tau-codim-conjectures-validation.witness.json).
In every case the strict inequality $1/\|C\|^2 < \tau(C_{\dim_q})$
holds.

**Honest framing: incomparability in general.**  The same script
also runs $50$ random Frobenius algebras with block counts in
$[2, 20]$ and parameters $d_q, \tau_p \in [0.5, 3]$.  In some of
these the Cauchy--Schwarz bound is in fact *stronger* than
$\tau(C_{\dim_q})$ (CS-to-Landauer ratio up to $\sim 4.9$ in the
sampled trials).  Hence the two bounds are **incomparable** in
general: this proposition does **not** claim Cauchy--Schwarz is
universally weaker, only that it is strictly weaker on the
balanced family — which is enough to rule out a CS-only proof of
the conjecture.

**Consequence for the Landauer conjecture.**  Any proof of
[`conj:tau-codim-landauer`](#conj:tau-codim-landauer) on the
balanced sub-family must use categorical or trace-positivity input
beyond the L${}^2$-Cauchy--Schwarz inequality.  Candidate routes
that survive:

1. **Centre-decomposition identity** $\tau(C^\dagger C) =
   \sum_\lambda 1/(d_q^2 \tau_p)$ combined with the AM-HM or
   AM-GM inequality on the block traces $\tau(p_\lambda)$;
2. **Frobenius-reciprocity argument** lifting the bound from the
   centre $Z(A)$ to the full algebra via the conditional
   expectation $E \colon A \to Z(A)$;
3. **Spectral lower bound** on the Laplacian
   $\Delta = m \circ m^* - \mathrm{id}_A$ in
   $\mathbf{Rep}(\mathcal{H}_q)$, exploiting the Frobenius-form
   positivity directly.

This proposition is therefore both a no-go (rules out
CS-only proofs on the balanced family) and a refinement of the
conjecture (narrows the search to the three categorical routes
above).
