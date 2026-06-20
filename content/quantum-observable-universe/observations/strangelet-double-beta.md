*Lean sibling: archimedean specialisation over $\mathbb{R}$ (AGENTS.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data.*

**Proposition.**
Let $\mathcal{S}$ be a strangelet and let $\mathfrak{p}$ be an
ordinary hadron interacting with it.  The interaction occurs in
the **degree-$2$ fiber** of the chiral fibration — the sector
governed by the cinquefoil $T_{2,5}^{\sigma}$ ($5$ crossings,
genus $2$).  This sector is electromagnetically dark: the
strangelet has $Q = 0$
([strangelet crossing energy](#prop\:strangelet-crossing-energy)),
so no photons are exchanged.

The interaction products become electromagnetically visible
only through **Skein crossing changes** — each crossing change
is a beta decay that lowers the degree from $2$ toward $1$.
The minimal path from the degree-$2$ fiber (cinquefoil,
$5$ crossings) to the degree-$1$ fiber (trefoil, $3$ crossings)
requires **two crossing changes**: a double beta decay.

**The Skein :refterm[descent]{#descent}.**

Each crossing change in the Skein relation

$$
  qL_+ - q^{-1}L_- = sL_0,
  \qquad s = q^{1/2} - q^{-1/2},
$$

produces an $L_0$ smoothing — a split into an electron (or
positron) and a neutrino
([beta decay products](#rem\:linking-relations-table)).
The amplitude for each crossing change is $s$.  Two crossing
changes give the double beta amplitude $s^2$ and rate $s^4$:

$$
  \Gamma_{2\beta}
   \propto 
  s^4
  = 
  (q^{1/2} - q^{-1/2})^4.
$$

At $q = q_0$:

$$
  s = 0.1041,
  \qquad
  s^2 = 0.01084,
  \qquad
  s^4 = 1.18 \times 10^{-4}.
$$

**The Skein amplitude is the EM/strong ratio.**

The Skein amplitude $s \approx 0.104$ is numerically
indistinguishable from the EM/strong ratio
$\tanh(\ln q) \approx 0.104$
([crossing energy decomposition](#prop\:crossing-energy-decomposition)).
This is not a coincidence: both measure the **antisymmetric
channel** of the $R$-matrix braiding.  Each crossing change
couples the degree-$2$ fiber to the degree-$1$ fiber through
the antisymmetric (electromagnetic) channel.  The double beta
decay rate is therefore

$$
  \Gamma_{2\beta}
   \sim 
  \left(\frac{\text{EM}}{\text{strong}}\right)^4
   \approx  10^{-4}.
$$

This is a **parameter-free prediction**: the suppression factor
is determined entirely by $q_0$.

**The intermediate state.**

The path through the Skein resolution tree is:

$$
  T_{2,5}^{\sigma}(5\text{ crossings})
  \xrightarrow{L_0}
  4_1(4\text{ crossings})
  \xrightarrow{L_0}
  T_{2,3}^{\sigma}(3\text{ crossings}).
$$

The intermediate knot is the **figure-eight** $4_1$ — the
amphichiral knot identified with the Higgs mass mechanism
([building block knots](#rem\:building-block-knots)).  Its
Jones polynomial at $q = q_0$ is $J(4_1) = 1.033$, close
to $1$ (the unknot value).  The intermediate state is
"almost trivial" — a fleeting Higgs-like excitation between
the two beta decays.

**The degree-$2$ to degree-$1$ fiber transition.**

The cinquefoil $T_{2,5}^{\sigma}$ lives on the
genus-$2$ part of Bring's surface: it wraps the surface with
winding $(2, 5)$, engaging two of the five sheets.  The trefoil
$T_{2,3}^{\sigma}$ lives on the genus-$1$ part: winding
$(2, 3)$, engaging the same two sheets but with fewer
crossings.

The double beta decay is a **fiber :refterm[descent]{#descent}**: the interaction
products, born in the genus-$2$ sector where electromagnetism
is absent ($Q = 0$), cascade through two Skein smoothings to
the genus-$1$ sector where electromagnetism is active
($Q \neq 0$).  Each smoothing peels off one electron-neutrino
pair and reduces the crossing number by one.

**Observable signature.**

The double beta decay of a strangelet interaction produces:

* **Two electrons** (or positrons), each from one $L_0$
  smoothing.
* **Two neutrinos** (or antineutrinos), one per smoothing.
* **Endpoint energy** $\sim 2q^{-1} \approx 1.80$ Skein
  units, or approximately $2.3$ MeV in physical units
  (scaling by $m_p c^2 / (V_B/\hbar_q^2)$).
* **Angular correlation** between the two electrons set by the
  Skein polynomial at the intermediate ($4_1$) vertex: the
  figure-eight's amphichirality ($4_1 = 4_1^{\sigma}$) means
  the correlation is **symmetric under parity**.

The $2.3$ MeV endpoint and the $s^4 \approx 10^{-4}$
suppression place this in the regime of **rare, low-energy
electron pair events** — detectable in underground
experiments designed for double beta decay searches
(GERDA, MAJORANA, nEXO, LEGEND).  The distinctive prediction:
the electron pair spectrum has a **parity-symmetric angular
distribution** (from the amphichiral intermediate) and an
endpoint set by $q^{-1}$, not by a nuclear mass difference.
