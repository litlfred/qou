*Overlap weighting changes only the energy, never the channel count:
every channel with $w > 0$ is occupied, so the active-set cardinality —
the bond order of [the CO LP dual](#prop:co-lp-dual-binding) — is
independent of the weights (Lean: `multipleBond_length`). The
equal-channel model ($w \equiv 1$) overbinds: for the $\sigma + 2\pi$
triple bond it gives $1.42\times$ the observed $D_0(\mathrm{N_2})$, while
a lateral weight $w_\perp \in [0.3, 0.7]$ brackets it (witness
`embeddable-knot-operator`).*
