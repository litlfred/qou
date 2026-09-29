import { paper, chapterRef } from "../schema/builders";

/**
 * Controlled Double-Slit Electron Diffraction
 *
 * Paper by Roger Bach, Damian Pope, Sy-Hwang Liou, and Herman Batelaan
 * (arXiv:1210.6243, New J. Phys. 15 (2013) 033018).
 * Full realization of Feynman's double-slit thought experiment with
 * controlled individual slits and single-electron buildup.
 */
export default paper({
  title: "Controlled Double-Slit Electron Diffraction",
  authors: [
    "Roger Bach",
    "Damian Pope",
    "Sy-Hwang Liou",
    "Herman Batelaan",
  ],
  affiliations: [
    "University of Nebraska-Lincoln",
    "Perimeter Institute for Theoretical Physics",
  ],
  date: "2013-03-13",
  abstract:
    "Double-slit diffraction is a corner stone of quantum mechanics. It " +
    "illustrates key features of quantum mechanics: interference and the " +
    "particle-wave duality of matter. In 1965, Richard Feynman presented " +
    "a thought experiment to show these features. Here we demonstrate the " +
    "full realization of his famous thought experiment. By placing a " +
    "movable mask in front of a double-slit to control the transmission " +
    "through the individual slits, probability distributions for single- " +
    "and double-slit arrangements were observed. Also, by recording " +
    "single electron detection events diffracting through a double-slit, " +
    "a diffraction pattern was built up from individual events.",
  macros: {},
  chapters: [
    chapterRef({ dir: "double-slit-experiment" }),
  ],
});
