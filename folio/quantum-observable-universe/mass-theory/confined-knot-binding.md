*Let $\beta \in H_3(R, q)$ be a confined nuclear braid built from crossing operators at generators $\sigma_{i_k}$. The Wedderburn-Artin decomposition separates each crossing's contribution into three channels:*

$$
  \hat{V}(c, d)
  = W_{\mathrm{sym}} \cdot \chi_{\mathrm{sym}}(c, d)
  + W_{\mathrm{std}} \cdot \chi_{\mathrm{std}}(c, d)
  + W_{\mathrm{alt}} \cdot \chi_{\mathrm{alt}}(c, d).
$$

*The extremal contributions exactly cancel for symmetric crossings encoding the proton-neutron force. The binding volume transfers entirely to the standard representation:*

$$
  \hat{V}_{\mathrm{pn}}
  = W_{\mathrm{std}} \cdot \Bigl(z - \frac{h_{\mathrm{A}}}{2}\Bigr).
$$

*The 2-dimensional standard representation creates non-commuting cross-channel interactions between adjacent generators. This generates the Markov-weighted pair interaction term $\delta_{\times}$.*

For an $A$-nucleon system constructed sequentially through quark, nucleon, and nuclear jet levels, the character ratio measures the volume departure from the free constituents. The total knot factor multiplies these strict, empirically-independent character ratios across all levels.

## The three levels are not in one convention

The product "across all levels" needs the three character ratios to be ratios of
the *same* functional. They are not. The quark and nucleon levels are Markov
traces — weights $y_\lambda$, convention D (Wenzl $r = 2$), which admits only
$\le 2$-row shapes. The nuclear-jet level is specified by
[$\tilde w_\lambda = \dim_q(\lambda)^2/[n]_q!$](#conj:jet-convergence-classical-limit),
over **all** partitions, and those are
[distinct families on every stratum](#prop:wedderburn-weight-canonical). On $H_3$:

| $\lambda$ | $y_\lambda$ (D) | $\tilde w_\lambda$ |
|---|---:|---:|
| $(3)$ | $0.505404226503931$ | $0.163383228056257$ |
| $(2,1)$ | $0.247297886748035$ | $0.660673773661173$ |
| $(1,1,1)$ | $0$ | $0.163383228056257$ |

$\sum_\lambda \dim(\lambda)\,y_\lambda = 1$ exactly, as a normalised trace must;
$\sum_\lambda \tilde w_\lambda = 0.98744$ at $q_0$. The $(1,1,1)$ row is
structural — convention D is the $\mathfrak{sl}_2$ point of the Ocneanu family,
so $y_\lambda = 0$ once $\lambda$ has more than two rows, while $\tilde w$ is a
ratio of positive quantum integers. **The jet measure charges a block the Markov
trace annihilates.**

The two disagree about the $pn$ bond in particular, and not by a rescale: the
single interface letter traces to $z + d_{pn} = 0.508229789376739$ under
$y$, and to $0.000071511999729$ under $\tilde w$ — a factor of $7107$, because
$\tilde w$ weights the two blocks equally and $d_{pn}$ is their midpoint up to
$\delta$, making $pn$ its near-null vector.

Together with the $A \ge 3$ ill-posedness of the jet word
([measured](#conj:jet-filtered-knot-factor)), the three-level product is not
evaluable as written. Either obstruction alone suffices.
