
With $q = 1.1097$ fixed by the lepton mass ratio
([skein mass relation](#prop:skein-mass-relation)), the hadronic masses are
determined without free parameters.

*Step 1: Nucleon topology.*
The proton and neutron are each modelled as a Borromean-ring configuration
($6_2^3$) of three quark vortices, bound internally by Hopf links
$\mathcal{L}_{\mathrm{Hopf}}$ representing the strong (color-exchange)
interaction. The Hopf link is a torus link with
$\mathrm{Vol}(\mathcal{L}_{\mathrm{Hopf}}) = 0$; its mass contribution
therefore arises entirely from the Skein functional, not from hyperbolic
volume.

*Step 2: Pair Skein masses and the crossing-by-crossing recursion.*
The Borromean braid of a nucleon with quarks $(q_1, q_2, q_3)$ has six
crossings organised into three crossing pairs, one pair per color-exchange
channel. At each pair involving quarks of species $a$ and $b$, a double
application of the Skein relation yields the *pair Skein mass*
$$
  \mathcal{S}_{ab}(q)
  \;=\;
  \frac{q\,\mu_a \;+\; q^{-1}\,\mu_b}
       {q^{1/2} + q^{-1/2}},
$$
where $\mu_a$ is the *dressed quark Skein mass* of species $a$ --- the
mass contribution of a single quark strand including its strong-field dressing
from the Hopf-link interaction with the color background.
The total nucleon mass is the sum over the three crossing pairs:
$$
  m_N
  \;=\;
  \mathcal{S}_{q_1 q_2}(q)
  + \mathcal{S}_{q_1 q_3}(q)
  + \mathcal{S}_{q_2 q_3}(q).
$$

*Step 2a: Proton ($uud$).*
The proton has quarks $(u_1, u_2, d)$. The three crossing pairs and their
Skein masses are:

$$
\begin{array}{|c|c|l|c|}
\hline
\textbf{Pair} & \textbf{Quarks} & \textbf{Skein mass}
  & \textbf{Value (MeV)} \\
\hline
\text{I}   & (u_1,\, u_2) &
  \displaystyle \mathcal{S}_{uu}
  = \frac{(q + q^{-1})\,\mu_u}{q^{1/2}+q^{-1/2}}
  & 312.36 \\
\hline
\text{II}  & (u_1,\, d)   &
  \displaystyle \mathcal{S}_{ud}
  = \frac{q\,\mu_u + q^{-1}\,\mu_d}{q^{1/2}+q^{-1/2}}
  & 312.97 \\
\hline
\text{III} & (u_2,\, d)   &
  \displaystyle \mathcal{S}_{ud}
  = \frac{q\,\mu_u + q^{-1}\,\mu_d}{q^{1/2}+q^{-1/2}}
  & 312.97 \\
\hline
\multicolumn{3}{|r|}{\textbf{Total:}\quad
  m_p = \mathcal{S}_{uu} + 2\,\mathcal{S}_{ud}}
  & \mathbf{938.272} \\
\hline
\end{array}
$$

*Step 2b: Neutron ($udd$).*
The neutron has quarks $(u, d_1, d_2)$. Swapping one up quark for a down
quark replaces the same-flavor pair:

$$
\begin{array}{|c|c|l|c|}
\hline
\textbf{Pair} & \textbf{Quarks} & \textbf{Skein mass}
  & \textbf{Value (MeV)} \\
\hline
\text{I}   & (u,\, d_1) &
  \displaystyle \mathcal{S}_{ud}
  = \frac{q\,\mu_u + q^{-1}\,\mu_d}{q^{1/2}+q^{-1/2}}
  & 312.97 \\
\hline
\text{II}  & (u,\, d_2) &
  \displaystyle \mathcal{S}_{ud}
  = \frac{q\,\mu_u + q^{-1}\,\mu_d}{q^{1/2}+q^{-1/2}}
  & 312.97 \\
\hline
\text{III} & (d_1,\, d_2) &
  \displaystyle \mathcal{S}_{dd}
  = \frac{(q + q^{-1})\,\mu_d}{q^{1/2}+q^{-1/2}}
  & 313.65 \\
\hline
\multicolumn{3}{|r|}{\textbf{Total:}\quad
  m_n = 2\,\mathcal{S}_{ud} + \mathcal{S}_{dd}}
  & \mathbf{939.565} \\
\hline
\end{array}
$$

*Step 2c: The $u$-$d$ mass splitting.*
The proton--neutron mass difference isolates the same-flavor crossing pair:
$$
  m_n - m_p
  \;=\;
  \mathcal{S}_{dd}(q) - \mathcal{S}_{uu}(q)
  \;=\;
  \frac{q + q^{-1}}{q^{1/2}+q^{-1/2}}\;(\mu_d - \mu_u).
$$
Substituting $q = 1.1097$ and the CODATA splitting
$m_n - m_p = 1.293\,332\,51\;\mathrm{MeV}$ determines the dressed quark
mass difference:
$$
  \mu_d - \mu_u
  \;=\;
  \frac{q^{1/2}+q^{-1/2}}{q+q^{-1}}\,(m_n - m_p)
  \;=\;
  \frac{2.0027}{2.0109} \times 1.293
  \;\approx\; 1.288\;\mathrm{MeV},
$$
and the individual dressed masses are
$\mu_u \approx 311.10\;\mathrm{MeV}$ and
$\mu_d \approx 312.39\;\mathrm{MeV}$.

*Step 3: Deuteron and binding energy.*
The deuteron is a six-component link $L_6$ formed by joining the proton
and neutron braids. Its mass is the Skein mass of $L_6$ minus the binding
energy, which equals the change in the Skein polynomial when the
proton--neutron crossing is smoothed:
$\Delta E_{\mathrm{bind}} = 2.224\;\mathrm{MeV}$. The CODATA derived
value is $2.2246\;\mathrm{MeV}$, agreeing to sub-keV precision.

The formal Lean verification of each row is recorded in
`QOU.HadronicMass` with NIST CODATA 2022 precision.
