These entries are the amplitudes of the $2\times 2$ Toffoli transfer matrix $\mathbf{M}(q)$, resolved by parity channel: index $6$ labels the even sector and index $7$ the odd sector. The diagonal amplitudes $P_{6,6}$ and $P_{7,7}$ are the **no-flip** (parity-preserving) amplitudes in the even and odd channels; the off-diagonal $P_{7,6}$ is the **target-flip** amplitude and $P_{6,7}$ its reverse. Evaluated at $z = q^3/(q^2+1)$ throughout.

| Entry | Formula |
|:-----:|---------|
| $P_{6,6}$ (no flip, even) | $\dfrac{(q^4+1)(q^4+q^2+2)}{4q(q^2+1)^2}$ |
| $P_{7,7}$ (no flip, odd) | $\dfrac{q^3(q^4+1)}{(q^2+1)^2}$ |
| $P_{7,6}$ (flip) | $-\dfrac{(q-1)(q+1)(q^6+q^4+2q^2+1)}{2q(q^2+1)^2}$ |
| $P_{6,7}$ (reverse flip) | $\dfrac{(q-1)(q+1)(2q^6+q^4+q^2+1)}{2q(q^2+1)^2}$ |

**The flip channel is not antisymmetric.** Reversing the transition does not yield $P_{6,7} = -P_{7,6}$: the two derived amplitudes carry distinct sextic factors $q^6+q^4+2q^2+1$ and $2q^6+q^4+q^2+1$, so $P_{6,7} + P_{7,6}$ vanishes only at $q = 1$ ([Toffoli transfer matrix](#prop:toffoli-transfer-matrix)).
