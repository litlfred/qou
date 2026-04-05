```tex
\begin{tikzcd}[
  row sep=2.2em, column sep=1.8em,
  every arrow/.append style={-stealth},
  every label/.append style={font=\scriptsize}
]
%% Main chapter flow (vertical)
\text{Ch\,1: QU axioms\\$(\mathbf{C},A,\tau)$}
  \arrow[d]
\\
\text{Ch\,2: QOU axioms\\observability, measurability,\\volume $\;\Rightarrow\;$ $\mathrm{SU}(2)$ emergence,\\Dirac operator}
  \arrow[d]
\\
\text{Ch\,3: Lifting obstructions\\Descartes condition $\chi=-6$\\brane tower, mass identity}
  \arrow[d]
\\
\text{Ch\,4: Braids \& knots\\particles as knots,\\topological mass}
  \arrow[d]
\\
\text{Ch\,5: Models\\Bring's surface $(g{=}4)$,\\Descartes theorem}
  \arrow[d]
\\
\text{Ch\,6: The Descartes Universe\\particle spectrum,\\nuclear physics}
  \arrow[d]
\\
\text{Ch\,7: Observations\\single parameter $q$,\\6-sig-fig predictions}
  \arrow[d]
\\
\text{Ch\,8: Information theory\\Turing completeness, $E=mc^2$}
%% SU(2) running-example thread (dashed)
\arrow[
  from=1-1, to=2-1,
  dashed, bend left=50,
  "\texttt{ex:*-su2}" description,
  start anchor=east, end anchor=east
]
\arrow[
  from=2-1, to=3-1,
  dashed, bend left=50,
  start anchor=east, end anchor=east
]
\arrow[
  from=3-1, to=4-1,
  dashed, bend left=50,
  start anchor=east, end anchor=east
]
\arrow[
  from=4-1, to=5-1,
  dashed, bend left=50,
  start anchor=east, end anchor=east
]
\end{tikzcd}
```
