```tex
\begin{tikzcd}[
  row sep=2.2em, column sep=1.8em,
  every arrow/.append style={-stealth},
  every label/.append style={font=\scriptsize}
]
%% Main chapter flow (vertical)
{\shortstack{Ch1: QU axioms\\$(\mathbf{C},A,\tau)$}}
  \arrow[d]
\\
{\shortstack{Ch2: QOU axioms\\observability, measurability,\\volume $\Rightarrow$ $\mathrm{SU}(2)$ emergence,\\Dirac operator}}
  \arrow[d]
\\
{\shortstack{Ch3: Lifting obstructions\\Descartes condition $\chi=-6$\\brane tower, mass identity}}
  \arrow[d]
\\
{\shortstack{Ch4: Braids \& knots\\particles as knots,\\topological mass}}
  \arrow[d]
\\
{\shortstack{Ch5: Models\\Bring's surface $(g{=}4)$,\\Descartes theorem}}
  \arrow[d]
\\
{\shortstack{Ch6: The Descartes Universe\\particle spectrum,\\nuclear physics}}
  \arrow[d]
\\
{\shortstack{Ch7: Observations\\single parameter $q$,\\6-sig-fig predictions}}
  \arrow[d]
\\
{\shortstack{Ch8: Information theory\\Turing completeness, $E=mc^2$}}
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

```tex
\clearpage
```
