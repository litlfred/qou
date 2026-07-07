We verify the [Frobenius relation](#prop:frobenius-relation) for $A = \mathcal{O}(\mathrm{SU}(2))$.

**Setup.** $A$ carries pointwise multiplication $\mu(f \otimes g) = f \cdot g$ and comultiplication $\Delta(f)(x, y) = f(xy)$.

**Concrete verification.** Evaluate both sides of $(\mu \otimes \mathrm{id}) \circ (\mathrm{id} \otimes \Delta) = \Delta \circ \mu$ on $f, h \in A$ at $(x, y, z)$.

- **Left side.** $(\mathrm{id} \otimes \Delta)(f \otimes h)(x, y, z) = f(x) h(yz)$. Applying $\mu \otimes \mathrm{id}$ gives $(f \cdot h_1)(x) h_2(z)$, where $\Delta(h) = \sum h_1 \otimes h_2$.
- **Right side.** $\Delta(\mu(f \otimes h))(x, z) = f(xz) h(xz)$.

Both sides evaluate to $f(xz) h(xz)$ because $\sum h_1(x) h_2(z) = h(xz)$.

**Interpretation.** Multiplying two functions and decomposing the product gives the same result as decomposing one function and then multiplying. The pointwise multiplication of functions is compatible with composing group elements.
