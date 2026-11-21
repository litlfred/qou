These entries are the amplitudes of the $2\times 2$ Toffoli transfer matrix $\mathbf{M}(q)$, resolved by parity channel: index $6$ labels the even sector and index $7$ the odd sector. The diagonal amplitudes $P_{6,6}$ and $P_{7,7}$ are the **no-flip** (parity-preserving) amplitudes in the even and odd channels; the off-diagonal $P_{7,6}$ is the **target-flip** amplitude and $P_{6,7}$ its reverse. Convention $z_D = q^3/(q^2+1)$ throughout.

| Entry | Formula |
|:-----:|---------|
| $P_{6,6}$ (no flip, even) | $\dfrac{(q^4+1)(q^4+q^2+2)}{4q(q^2+1)^2}$ |
| $P_{7,7}$ (no flip, odd) | $\dfrac{q^3(q^4+1)}{(q^2+1)^2}$ |
| $P_{7,6}$ (flip) | $-\dfrac{(q-1)(q+1)(q^6+q^4+2q^2+1)}{2q(q^2+1)^2}$ |
| $P_{6,7}$ (reverse flip) | $\dfrac{(q-1)(q+1)(2q^6+q^4+q^2+1)}{2q(q^2+1)^2}$ |

**The flip channel is not antisymmetric.** One might expect $P_{6,7} = -P_{7,6}$, on the grounds that reversing the crossing negates it. The two derived amplitudes differ by more than a sign — their sextic factors are $q^6+q^4+2q^2+1$ and $2q^6+q^4+q^2+1$ — so $P_{6,7} \neq -P_{7,6}$. This is not a convention artefact: the antisymmetry fails under $C$ and under $D$ alike. $\Phi$ itself is withdrawn; it is not in the image of the Toffoli construction ([Toffoli transfer matrix](#prop:toffoli-transfer-matrix)).
