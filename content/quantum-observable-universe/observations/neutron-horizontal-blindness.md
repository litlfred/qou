**Remark.** Specialising the symbolic $\gamma^{(4)} \cdot \mathfrak{N}$
computation to the two flavor choices gives contrasting
$[e^-]$-channel responses:

$$
  \mathrm{proton}\ (u,u,d)
  \colon \quad
  [e^-]
  =
  \bigl(\tfrac{H_A^6}{4} + \tfrac{H_A^4}{4} - H_A^2\bigr)
  + \varphi_0 \bigl(\tfrac{H_A^7}{4} + \tfrac{3H_A^5}{4}\bigr)
  + \varphi_1 \bigl(\ldots\bigr)
  + \varphi_{01} \bigl(\ldots\bigr),
$$

$$
  \mathrm{neutron}\ (u,d,d)
  \colon \quad
  [e^-]
  =
  \bigl(-\tfrac{H_A^4}{4} - H_A^2\bigr)
  + \varphi_0 \cdot 0
  + \varphi_1 \bigl(-\tfrac{H_A^7}{4} - \tfrac{3H_A^5}{2} - 2H_A^3\bigr)
  + \varphi_{01} \bigl(\tfrac{H_A^6}{4} + \tfrac{5H_A^4}{4} + H_A^2\bigr).
$$

The $\varphi_0$ coefficient in the neutron case is identically zero
as a polynomial in $H_A$: the horizontal linear polarisation
contributes nothing to the pair-creation channel for scattering off
a neutron.  This follows from the flavor structure $(u,d,d)$: the
$\sigma_0$-generator couples quarks $1 \leftrightarrow 2$ (a
$u$-$d$ pair) and $1 \leftrightarrow 3$ (another $u$-$d$ pair),
both carrying $\varepsilon = H_A/2$, whose contributions cancel
exactly under reduction to NF in the $[e^-]$ row.  For the proton
$(u,u,d)$ the same cancellation fails because quark pair
$1\leftrightarrow 2$ is $u$-$u$ ($\varepsilon = 0$), breaking the
symmetry.

**Testable flavor-selective pair creation.** A polarised
$\gamma$-beam tagged by horizontal polarisation ($\varphi_0 \neq 0$,
$\varphi_1 = \varphi_{01} = 0$) should produce $e^-e^+$ pairs when
scattered off a proton target but not off a free neutron.  The
vertical-polarisation ($\varphi_1$) and Hopf-dressed ($\varphi_{01}$)
channels remain open for both nucleons, so the predicted signature
is a $\cos(2\phi)$ azimuthal asymmetry in $\gamma + \mathfrak{p}$
pair production that *disappears* in $\gamma + \mathfrak{n}$ pair
production at the same incident polarisation.

**Nuclear context.** Inside a bound nucleus, isospin mixing mediated
by inter-nucleon crossings should restore the $\varphi_0$ channel,
yielding a mixing fraction that tracks $Z/A$.  This is consistent
with the empirical observation that proton-rich isotopes are more
efficient converters of polarised $\gamma$-radiation than
neutron-rich isotopes — a pattern usually attributed to Coulomb
field strength, but in QOU explained purely by the Hecke flavor
algebra.

**Witness:** `gamma4-hits-proton-quark-words.py` (neutron
specialisation in the `gamma4_neutron_specialised_udd` block).
