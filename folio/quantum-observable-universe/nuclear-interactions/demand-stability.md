*The derived atom $\mathcal{A}(Z, N)$ is:*

1. ***Beta-stable** if and only if, for all single nucleon exchanges $\mathfrak{p} \leftrightarrow \mathfrak{n}$ at fixed $A = Z + N$:*

$$
  |\mathrm{dem}(\mathcal{A}(Z, N))|
  \;\leq\;
  |\mathrm{dem}(\mathcal{A}(Z \pm 1, N \mp 1))|.
$$

*The stable configuration minimizes the demand magnitude at fixed $A$.*

2. ***Shell-closed** if and only if $\mathrm{dem}(\mathcal{A}) = \varnothing$. All NF coefficients are non-negative.*
3. ***Doubly magic** if both the nucleus $\mathcal{N}(Z, N)$ and the atom $\mathcal{A}(Z, N)$ have locally minimal Markov trace $\mathrm{tr}_M$ among neighboring $(Z, N)$.*

The demand-free ${}^3\mathrm{He}$ and the Markov-trace-minimal ${}^4\mathrm{He}$ represent two distinct stability mechanisms: shell closure (zero demand) and action minimization (lowest trace).

## Connection to beta decay

The $e^-$ demand channel in the nucleon normal form represents beta decay balance. A nucleon with $c_{e^-} < 0$ is topologically configured to emit an electron. The transition $\mathfrak{n} \to \mathfrak{p} + e^- + \bar\nu$ occurs when:

$$
  |c_{e^-}(\mathfrak{n})| > |c_{e^-}(\mathfrak{p})|
  \quad \text{and} \quad
  \mathrm{net}(\mathfrak{n}) < \mathrm{net}(\mathfrak{p}).
$$

At $q_0$, both conditions hold. Thus, the free neutron beta-decays.

## Inductive scaling via transfer matrix identities

For nuclei with $A > 4$, the NF computation scales polynomially via inductive Gröbner--Shirshov reduction. The key identity is the transfer matrix factorization: the product of two inter-nucleon crossings reduces via the Hecke relation before the next nucleon is appended. For same-type nucleon pairs:

$$
  C_{pp} \cdot C_{pp} = h_{\mathrm{A}} \cdot C_{pp} + \mathbf{1},
  \qquad
  C_{nn} \cdot C_{nn} = \mathbf{1} - h_{\mathrm{A}} \cdot C_{nn}.
$$

These are instances of the Hecke relation $\sigma_i^2 = h_{\mathrm{A}} \sigma_i + \mathbf{1}$ applied to typed crossings. They ensure that iterated same-type nucleon pairs do not increase the NF complexity beyond linear growth in the number of nucleons.

## Witness scope and multi-precision grid (`all-nuclides-sdp-admissibility-mp`)

The companion witness [`computations/all-nuclides-sdp-admissibility-mp.witness.json`](../../../computations/all-nuclides-sdp-admissibility-mp.witness.json), produced by [`computations/all_nuclides_sdp_admissibility_mp.py`](../../../computations/all_nuclides_sdp_admissibility_mp.py) at `mpmath` 50 dps (+10 guard digits) with MPFR decimal-string transport to `solve_operator_selection_lp`, supersedes the legacy float64 sweep:

- **Superseded float64 AME2020 sweep (`3,558` rows):** native float64 `build_atom_nf` overflowed on $1{,}337 / 3{,}558$ nuclides ($37.6\,\%$) for $A \ge 163$, leaving $0 / 43$ isotopes solvable at the magic proton number $Z = 82$ (e.g., ${}^{208}\mathrm{Pb}$ reaches $\mathrm{nf}_{\mathrm{net}} \approx -1.2483 \times 10^{499}$, ~191 orders beyond IEEE 754 binary64).
- **Multi-precision synthetic magic-$Z$-dense $(Z, N)$ grid (`4,932` rows):** evaluates $Z \in [0, 92]$, with full $N \in [0, 160]$ scans ($161 / 161$ rows solved) at every magic proton shell $Z \in \{2, 8, 20, 28, 50, 82\}$ and $47$ neutron-number points per non-magic $Z$ (including $93 / 93$ rows solved at every magic neutron shell $N \in \{2, 8, 20, 28, 50, 82, 126\}$), achieving `nf_overflow_count = 0` and `rows_carrying_mpfr_dual = 4,932`.
- **Population scope:** this witness covers the synthetic magic-$Z$-dense $(Z, N)$ grid up to $Z_{\max} = 92$, $N_{\max} = 160$ rather than the empirical AME2020 nuclide list; proton shell $Z = 126$ lies outside the $Z \le 92$ grid range (`0 / 0` rows), while neutron shell $N = 126$ is covered across all $93$ proton numbers.
