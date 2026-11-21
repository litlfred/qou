The [Frobenius relation](#prop:frobenius-relation) is checked here for $A = \mathcal{O}(\mathrm{SU}(2))$.

**Setup.** $A$ carries pointwise multiplication $\mu(f \otimes g) = f \cdot g$. The comultiplication $\Delta_\mu$ dual to $\mu$ under the Haar [Frobenius pairing](#def:frobenius-pairing) $\langle f, g \rangle = \int_{\mathrm{SU}(2)} f g$ is the *diagonal* comultiplication, characterised by

$$
\langle \Delta_\mu(f),\, g \otimes h \rangle = \langle f,\, g h \rangle = \int_{\mathrm{SU}(2)} f\, g\, h .
$$

Equivalently $\Delta_\mu(f)(x, y) = f(x)\,\delta_{x = y}$: it is supported on the diagonal — a distribution for the continuous group, a genuine element of $A \otimes A$ for any finite group. Note that $\Delta_\mu$ is **not** the Hopf group-comultiplication $f \mapsto f(xy)$; that map is a bialgebra structure, not the Frobenius comultiplication dual to $\mu$.

**Concrete verification.** Evaluate both sides of $(\mu \otimes \mathrm{id}) \circ (\mathrm{id} \otimes \Delta_\mu) = \Delta_\mu \circ \mu$ on $f, h \in A$.

- **Left side.** $(\mathrm{id} \otimes \Delta_\mu)(f \otimes h)(x, y, z) = f(x)\, h(y)\, \delta_{y = z}$. Applying $\mu \otimes \mathrm{id}$ multiplies the first two tensor factors ($x = y$), giving $(f \cdot h)(x)\, \delta_{x = z}$.
- **Right side.** $\Delta_\mu(\mu(f \otimes h))(x, z) = \Delta_\mu(f \cdot h)(x, z) = (f \cdot h)(x)\, \delta_{x = z}$.

Both sides equal $(f \cdot h)(x)\, \delta_{x = z}$, so the Frobenius relation holds.

**Interpretation.** The diagonal comultiplication records a function together with the constraint that its two output copies coincide. Multiplying two functions and then duplicating along the diagonal gives the same diagonal-supported element as duplicating one factor first and then multiplying — the compatibility of $\mu$ with the pairing-dual $\Delta_\mu$ that makes $A$ a Frobenius algebra.
