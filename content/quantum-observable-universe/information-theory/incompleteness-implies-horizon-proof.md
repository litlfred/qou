Define the **diagonal function**

$$
  d(n) \;=\; \mathrm{eval}(e(n))(n) + 1.
$$

For any program $p \in P$, surjectivity gives $n$ with
$e(n) = p$.  Then

$$
  d(n) = \mathrm{eval}(p)(n) + 1 \neq \mathrm{eval}(p)(n),
$$

so $d \neq \mathrm{eval}(p)$.  Since $p$ was arbitrary,
$d \notin \mathrm{im}(\mathrm{eval})$.
$\qquad\blacksquare$
