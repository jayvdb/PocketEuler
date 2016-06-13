/**
 * @fileoverview Local remark configuration.
 */

module.exports = {
  "plugins": {
    "lint": {
      // config common with other tools
      "heading-style": false,  // MD003
      "list-item-bullet-indent": false,  // MD006 & MD007
      "hard-break-spaces": false,  // MD009
      "no-tabs": false,  // MD010
      "no-consecutive-blank-lines": false,  // MD012
      "maximum-line-length": 250,  // MD013
      "no-multiple-toplevel-headings": false,  // MD025
      "no-html": false,  // MD033
      "no-inline-padding": false,  // MD038

      // config explicitly stating defaults
      "ordered-list-marker-value": "ordered",  // MD029

      // config for remark-lint only
      "list-item-indent": "space",
      "no-shortcut-reference-link": false,
      "no-undefined-references": false,
      "list-item-spacing": false,
      "code-block-style": false,
      "emphasis-marker": false,
      "dummy": false
    }
  }
}
