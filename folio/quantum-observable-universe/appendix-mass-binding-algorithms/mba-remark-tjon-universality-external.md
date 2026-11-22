The many-body magnitude leg of $\Delta_\lambda$ is scored against an external
observable — the empirical correlation between three-body and four-body binding
energies, known in nuclear physics as the *Tjon line*. The folio carries no
statement of what that literature actually establishes, which leaves an analogy
free to be read as an established premise. This remark states the external
result, states the corpus construction, and separates them.

## The external results

Two results are used.

**No four-body parameter at leading order.** Working in an effective theory of
short-range interactions whose two-body scattering length $a$ is large
compared with the natural low-energy length scale $\ell$ of the interaction
($|a| \gg \ell$), Platter, Hammer and Meißner find that an $\mathrm{SU}(4)$-symmetric
*one-parameter* three-nucleon interaction suffices to renormalise the
four-nucleon system at leading order in $\ell/|a|$; the empirical
triton–$\alpha$ correlation then ``follows immediately'', swept out by varying
that single three-body parameter \cite{platter2005tjon}. With
the binding energies $B(^2\mathrm{H}) = 2.22$ MeV and
$B(^3\mathrm{H}) = 8.48$ MeV as inputs they obtain
a binding energy $B(\alpha) \approx 29.5$ MeV for the $\alpha$-particle, against a Coulomb-corrected
experimental $29.0 \pm 0.1$ MeV.

**A dimensionless four-to-three ratio.** Solving the four-boson Yakubovsky
equations with no four-body parameter at all, Hammer and Platter report that
away from threshold the four-body ground state and the deepest three-body state
are related by a factor of $5$ \cite{hammer2007fourbody}. The correlation is
approximately linear away from threshold for either sign of $a$, with positive
curvature for $a > 0$ and negative curvature for $a < 0$; the nonlinearity is
confined to the threshold region.

## Limits of the external results

Each of the following is a separate statement that the results above do
**not** license, and the distinctions matter because the corpus scores against
these numbers.

1. **``No four-body parameter is needed'' is not ``no four-body force exists.''**
   The first is a statement about what a calculation requires for
   renormalisation; the second is a statement about nature. The four-nucleon
   force is *small*, not absent: Jurgenson, Navrátil and Furnstahl measure the
   similarity-renormalisation-group-induced four-body contribution at
   $^4\mathrm{He}$ as a net effect of order tens of keV, with the long-range
   N$^3$LO estimate of order a few hundred keV \cite{jurgenson2009srg}.

2. **The leading-order claim is contested.** Yamashita et al. find a strong
   sensitivity of the deepest four-body energy to a four-body subtraction
   constant, and conclude that a four-body parameter should generally enter at
   leading order. The disagreement is recorded in \cite{hammer2007fourbody}
   itself, which also notes that Yamashita et al. hold four-body systems of
   $^4\mathrm{He}$ atoms and nucleons to be special cases *where this
   sensitivity is absent*, repulsive interactions suppressing the probability
   of four particles being close together. So for the nuclear case both sides
   agree; for the general case they do not, and \cite{hammer2007fourbody}
   stresses that its universality rests on the renormalisation-group analysis
   it inherits.

3. **The zero-range limit is not the nuclear regime.** The universal ratio $5$
   is a zero-range result. Nature, from AME2020 \cite{ame2020}, gives
   $B(^4\mathrm{He})/B(^3\mathrm{H}) \approx 3.42$ after
   Coulomb correction. The gap is expected:
   \cite{platter2005tjon} states that its leading-order Tjon line is shifted
   from the empirical one precisely because finite-range effects are neglected.

## Inequivalence with the simplex condition

The magnitude sidecar expands the many-body binding moment in a
simplex (inclusion–exclusion) basis,

$$
  M(A) \;=\; \sum_k \mu_k \binom{A}{k},
$$

in which ``no four-body parameter'' reads as the single condition $\mu_4 = 0$,
equivalent to $M(4) = 4M(3) - 6M(2)$. It is tempting to read the external
result as *establishing* that condition. It does not, and the two are provably
inequivalent.

On the $\mu_4 = 0$ baseline the four-to-three ratio obeys
$M(4) < 4\,M(3)$ *strictly*, for any $\mu_2 > 0$ and whatever $\mu_3$ may be —
the gap is exactly $-6\mu_2$. The universal ratio $5$ therefore lies outside
the baseline's reachable range altogether, so a calculation carrying no
four-body input at all can sit at a ratio the simplex condition cannot produce.
Conversely, feeding $M(4) = 5\,M(3)$ into the basis returns

$$
  \mu_4 \;=\; 9\mu_2 + \mu_3,
$$

which at the nuclear $(\mu_2, \mu_3)$ is $\approx 9.81$ — some $2.6$ times the
value the nuclear data themselves produce. The fourth moment is therefore
*largest* in the calculation that contains no four-body input, which is a
direct statement that $\mu_4$'s magnitude is an artifact of the basis rather
than a measurement of four-body physics.

There is a blunter way to see the same thing, and it should be stated because
the name invites the opposite reading. Three moments are fitted to three
anchors ($A = 2, 3, 4$), so the system is exactly determined and

$$
  \mu_4 \;:=\; M(4) - 4M(3) + 6M(2)
$$

is a *definition*, carrying zero residual freedom. Writing $\mu_4$ is therefore
another way of writing ``the amount by which $M(4)$ exceeds the two-point
prediction'', and nothing more. It is not a measurement of a four-body
interaction, and calling it ``the four-body moment'' — as the surrounding
literature's vocabulary tempts one to — asserts an identification that no step
above establishes. The corpus rule this instantiates is
*defined residual $\neq$ derived decomposition*: a residual introduced with
$:=$ acquires no physical content from the index it is written under.

Both facts are formalised over a generic commutative ring, in
`QOU.MassTheory.TjonSimplexForm` — `tjon_baseline_lt_four_ratio`,
`universal_ratio_not_in_tjon_baseline` and `universal_ratio_forces_mu4` — and
measured in `computations/deltalambda/tjon_external_cross_check_probe.py`.

The consequence for the magnitude leg is a constraint on citation, not a new
result. The external literature may be cited for why a nonzero $\mu_4$ is
worth attending to at all — it registers a real departure of $M(4)$ from the
two-point prediction, which is information about the binding curve — and never
as a derivation of the simplex form, nor as licence to read that departure as
four-body physics.
