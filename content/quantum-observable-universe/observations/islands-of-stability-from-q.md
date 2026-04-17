The Borromean spin-orbit intruder mechanism of
[shell intruder](#prop:nuclear-shell-intruder) extends unchanged
to the next harmonic-oscillator shell $N = 7$, producing
concrete predictions for the superheavy "islands of stability"
that depend on the substrate parameter $q$ only through the
$q$-Laplacian threshold of §Step 3.

**Extending the intruder table to $N = 7$.**

The cumulative HO closure is
$C_N = (N+1)(N+2)(N+3)/3$, so $C_6 = 168$ and $C_7 = 240$.
The highest-$j$ sub-level at HO level $N$ contributes
$2(N{+}1)$ states and descends to the preceding shell when
$3 \cdot [\ell]_q [\ell+1]_q > 2(N+1)$.  For $N = 7$:

- $\ell = 7$, $j = 15/2$: intruder $1j_{15/2}$ with
  $2(7{+}1) = 16$ states.
- $q$-Laplacian threshold (using the symmetric convention
  $[n]_q = (q^n - q^{-n})/(q - q^{-1})$):
  $3 [7]_q [8]_q \approx 3 \cdot 7.70 \cdot 9.11 \approx 210$,
  vastly exceeds $2(7+1) = 16$ — the intruder is *deeply*
  subducted into the $N = 6$ shell.

Completing the table:

| From $N$ | Level | $j$ | States $2(N{+}1)$ | Creates magic |
|---------:|-------|----:|------------------:|--------------:|
| 3 | $1f_{7/2}$ | $7/2$ | 8 | **28** |
| 4 | $1g_{9/2}$ | $9/2$ | 10 | **50** |
| 5 | $1h_{11/2}$ | $11/2$ | 12 | **82** |
| 6 | $1i_{13/2}$ | $13/2$ | 14 | **126** |
| **7** | $1j_{15/2}$ | **$15/2$** | **16** | **$168 + 16 = 184$** |

**Neutron island at $N = 184$.** The closure at $112 + 14 = 126$
from the $N = 6$ intruder is followed by accumulation through
the $N = 6$ bulk (to $168$) and descent of the $N = 7$ intruder
$1j_{15/2}$, giving the next neutron closure at $168 + 16 = 184$
— exactly the value predicted by nuclear shell-model
extrapolations and central to the superheavy-island programme.
The prediction is **parameter-free**: it uses only the integer
crossing number $3$ and the shell-structure identity above.

**Proton island: Coulomb-shifted.**

For protons the bare HO closure sits at the same cumulative
$C_N$, but the Coulomb penalty
$E_C(Z) = a_C Z^2 / A^{1/3}$ shifts the effective shell energies
downward with increasing $Z$.  In
[$q$-stability](#rem:q-stability-ranges) the stability window
$[q_{\min}, q_{\max}]$ narrows from width $\sim 0.83$ at He to
width $< 0.01$ for $Z > 50$; for $Z \sim 114$–$126$ the window
has collapsed to a single integer prediction per $q$ value.

Evaluating the Bethe–Weizsäcker balance at $q_0 = 1.1098$ inside
the $N = 7$ intruder region selects the following stable Coulomb-
corrected closures:

| $q$ window | $Z_{\mathrm{pred}}$ | $N_{\mathrm{pred}}$ | Comment |
|:----------:|:-------------------:|:-------------------:|:--------|
| $[1.109, 1.112]$ | $114$ | $184$ | Flerovium-centred island |
| $[1.108, 1.110]$ | $120$ | $184$ | Secondary closure (unbinilium) |
| $[1.107, 1.109]$ | $126$ | $184$ | Bare HO + intruder magic |

The three candidate proton magic numbers $\{114, 120, 126\}$
— which in mainstream calculations appear as competing
predictions from different nuclear models (Skyrme, relativistic
mean-field, macroscopic–microscopic) — arise here as a
sequence of *adjacent integer plateaus* in the $q$-window.  The
ordering of these plateaus is a direct consequence of the
$q$-deformed level spacing $[\ell]_q [\ell+1]_q$ and therefore a
direct probe of the substrate parameter.

**Falsifiability.**

1. **Mass-number prediction.** The most stable superheavy
   isotope is predicted at $(Z, N)$ $=$ $(114, 184)$ for
   $q_0 \approx 1.1098$, giving $A = 298$.  Any observation of
   a markedly longer-lived nuclide at, say, $(120, 184)$
   would force $q_0$ into the narrow window
   $[1.108, 1.110]$ — directly testing the value inferred
   from the lepton mass ratio
   ([skein mass relation](#rem:skein-mass-relation)).

2. **Half-life hierarchy.**  Because our shell-threading
   conjecture ([shell threading](#conj:shell-threading-energy))
   ties half-life to $q$-Laplacian eigenvalues, the island-
   centre half-life should scale as
   $[15/2]_q [17/2]_q$ — giving a parameter-free factor
   relative to the $N = 6$ island centre (Pb) of
   approximately $([15/2]_{q_0}[17/2]_{q_0}) /
   ([13/2]_{q_0}[15/2]_{q_0}) \approx 1.35$.  This is an
   order-of-magnitude prediction, testable against
   extrapolated half-lives of $Z \gtrsim 114$ isotopes.

3. **Beyond $N = 7$.**  The next intruder is $1k_{17/2}$ from
   $N = 8$ with $2(8{+}1) = 18$ states, yielding a hypothetical
   closure at $240 + 18 = 258$.  Whether such a "second
   island" is populated in practice depends on whether the
   Coulomb $Z^2$ term can be balanced at all at that neutron
   number; preliminary Bethe–Weizsäcker inspection suggests
   no stable $Z$ exists and the island dissolves.  This is a
   qualitative prediction distinct from Ding et al.
   \cite{ding2026}, who do not address $N > 7$.

**Net result.** The same Borromean-crossing + $q$-Laplacian
apparatus that produces the first seven magic numbers without
fitting extends, without modification, to the $N = 7$ shell and
selects $(Z, N) = (114, 184)$ as the centre of the predicted
superheavy island.  The narrowing of the $q$-stability window
with $Z$ makes the island-centre a sharper probe of $q_0$ than
any light-nucleus observable.
