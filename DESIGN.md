---
name: Obsidian Precision
colors:
  surface: '#10141a'
  surface-dim: '#10141a'
  surface-bright: '#353940'
  surface-container-lowest: '#0a0e14'
  surface-container-low: '#181c22'
  surface-container: '#1c2026'
  surface-container-high: '#262a31'
  surface-container-highest: '#31353c'
  on-surface: '#dfe2eb'
  on-surface-variant: '#e4beba'
  inverse-surface: '#dfe2eb'
  inverse-on-surface: '#2d3137'
  outline: '#ab8986'
  outline-variant: '#5b403e'
  surface-tint: '#ffb3ad'
  primary: '#ffb3ad'
  on-primary: '#68000a'
  primary-container: '#ff5451'
  on-primary-container: '#5c0008'
  inverse-primary: '#b91a24'
  secondary: '#4edea3'
  on-secondary: '#003824'
  secondary-container: '#00a572'
  on-secondary-container: '#00311f'
  tertiary: '#7bd0ff'
  on-tertiary: '#00354a'
  tertiary-container: '#009bd1'
  on-tertiary-container: '#002d40'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#ffdad7'
  primary-fixed-dim: '#ffb3ad'
  on-primary-fixed: '#410004'
  on-primary-fixed-variant: '#930013'
  secondary-fixed: '#6ffbbe'
  secondary-fixed-dim: '#4edea3'
  on-secondary-fixed: '#002113'
  on-secondary-fixed-variant: '#005236'
  tertiary-fixed: '#c4e7ff'
  tertiary-fixed-dim: '#7bd0ff'
  on-tertiary-fixed: '#001e2c'
  on-tertiary-fixed-variant: '#004c69'
  background: '#10141a'
  on-background: '#dfe2eb'
  surface-variant: '#31353c'
typography:
  headline-xl:
    fontFamily: geist
    fontSize: 28px
    fontWeight: '600'
    lineHeight: 36px
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: geist
    fontSize: 20px
    fontWeight: '600'
    lineHeight: 28px
    letterSpacing: -0.015em
  headline-md:
    fontFamily: geist
    fontSize: 16px
    fontWeight: '600'
    lineHeight: 24px
    letterSpacing: -0.01em
  body-lg:
    fontFamily: geist
    fontSize: 14px
    fontWeight: '400'
    lineHeight: 20px
    letterSpacing: -0.005em
  body-md:
    fontFamily: geist
    fontSize: 13px
    fontWeight: '400'
    lineHeight: 18px
    letterSpacing: 0em
  body-sm:
    fontFamily: geist
    fontSize: 12px
    fontWeight: '400'
    lineHeight: 16px
    letterSpacing: 0.005em
  code-lg:
    fontFamily: jetbrainsMono
    fontSize: 14px
    fontWeight: '400'
    lineHeight: 22px
    letterSpacing: 0em
  code-md:
    fontFamily: jetbrainsMono
    fontSize: 13px
    fontWeight: '400'
    lineHeight: 20px
    letterSpacing: 0em
  code-sm:
    fontFamily: jetbrainsMono
    fontSize: 11px
    fontWeight: '400'
    lineHeight: 16px
    letterSpacing: 0em
  label-md:
    fontFamily: jetbrainsMono
    fontSize: 12px
    fontWeight: '500'
    lineHeight: 16px
    letterSpacing: 0.02em
  label-sm:
    fontFamily: jetbrainsMono
    fontSize: 10px
    fontWeight: '600'
    lineHeight: 14px
    letterSpacing: 0.04em
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  space-0: 0px
  space-1: 2px
  space-2: 4px
  space-3: 6px
  space-4: 8px
  space-6: 12px
  space-8: 16px
  space-10: 20px
  space-12: 24px
  space-16: 32px
  gutter-editor: 12px
  sidebar-width: 260px
  rail-width: 48px
  tab-height: 36px
  status-height: 24px
---

## Brand & Style

This design system establishes an ultra-focused, distraction-free environment for high-stakes engineering workflows. Built around the ethos of technical precision and cognitive clarity, the interface disappears into the background, elevating the engineer’s code and execution flow to the foreground.

The aesthetic fuses **technical minimalism** with refined **developer-tool utilitarianism**. It avoids superficial visual noise—such as heavy glows or expressive rounded forms—in favor of structural discipline, hairline dividers, strict spatial rhythm, and high-legibility typographic hierarchies. An intense, high-energy crimson serves as a deliberate operational catalyst, reserved exclusively for irreversible or execution-centric commands like running builds, compiling binaries, or live deployment.

The interface evokes uncompromising focus, structural authority, zero-latency feedback, and professional rigor.

## Colors

The palette relies on a multi-tiered slate/obsidian dark architecture paired with functional syntax and telemetry tokens.

- **Primary Accent (`#ef4444` / Crimson Active):** High-energy red dedicated strictly to primary trigger operations (`Run`, `Build`, `Commit & Push`). It commands visual urgency without polluting passive states.
- **Secondary Status (`#10b981` / Emerald Terminal):** Reserved for pass states, active process daemons, zero-error telemetry, and live execution status.
- **Tertiary Accent (`#38bdf8` / Sky Info):** Designates active symbolic links, information tokens, file branch badges, and active inspection tabs.
- **Warning Indicator (`#f59e0b` / Amber Alert):** Handles compilation warnings, unresolved debt, and lint diagnostics.
- **Neutral Foundation:**
  - `Canvas Deepest`: `#090d13` (Terminal backplanes, collapsed drawers, utility docks).
  - `Canvas Base`: `#0d1117` (Active code editor surface, primary workspace pane).
  - `Canvas Elevated`: `#161b22` (Sidebar panels, file navigator, tab strips, top menu navigation).
  - `Canvas Overlay`: `#21262d` (Hover states, context menus, command palette overlays).
  - `Border Subtle`: `#30363d` (Structural hairline separations, gutter splits).
  - `Border Focus`: `#8b949e` (Keyboard navigation boundaries, active panel outlines).
  - `Text Primary`: `#f0f6fc` (Code tokens, active file headers, primary readouts).
  - `Text Secondary`: `#8b949e` (Line numbers, breadcrumb inactive segments, panel descriptions).
  - `Text Muted`: `#484f58` (Inactive comments, disabled states, tab close icons).

## Typography

The type ecosystem establishes a dual-font structure:

1. **System & Frame Typography (`Geist`):** Delivers clean geometry and neutral legibility across structural chrome, sidebars, context panels, settings views, and modal headers. Optical sizing ensures compact labels remain readable without encroaching on code space.
2. **Code & Telemetry Typography (`JetBrains Mono`):** Applied to the primary code buffer, terminal shells, line numbering, diff changes, memory addresses, and status chips. Tabular numbers (`tnum`) and code ligatures are enabled across all monospaced roles.

Text renders with `subpixel-antialiased` smoothing optimized for high-density, low-luminance dark backgrounds.

## Layout & Spacing

The layout model is an absolute-pinned, multi-pane workbench optimized for window-filling desktop workflows:

- **Structural Grid & Panes:** Zero margins at the browser frame. The layout relies on flexbox and CSS Grid divisions bounded by single-pixel rules (`#30363d`).
  - **Activity Rail (Far Left):** Fixed `48px` width.
  - **Primary Tree/Navigator Sidebar:** Collapsible, default `260px` with fluid manual drag resizing (`min: 180px`, `max: 480px`).
  - **Editor Stage:** Flex-grow central canvas, subdivided horizontally or vertically with split gutters.
  - **Console / Terminal Drawer:** Bottom docked, vertically resizable (`min: 120px`, `max: 60vh`).
  - **Status Footbar:** Fixed `24px` continuous strip pinned to screen edge.
- **Rhythm & Padding:** Component spacing conforms to a dense 4px base increment. Tab items, tree nodes, and terminal rows enforce strict horizontal alignments:
  - File tree rows: `24px` height with `6px` left indentation per depth level.
  - Line numbers gutter: `40px` to `56px` fixed width with right-aligned glyphs and `12px` offset before text onset.

## Elevation & Depth

This design system avoids diffused drop shadows and ambient blurs. Depth is communicated strictly via **tonal planar stepping** and **hairline edge definition**.

- **Level 0 (Recessed Core - `#090d13`):** Terminal output wells, inactive dock panels, search inputs. Surrounded by an interior boundary of `1px solid #30363d`.
- **Level 1 (Primary Workspace - `#0d1117`):** Active editing surface, gutter regions. Clean, flush plane.
- **Level 2 (Navigation Chrome - `#161b22`):** Primary tab strip, left/right auxiliary sidebars, toolbar bands. Separated from Level 1 by continuous `1px solid #30363d` edge lines.
- **Level 3 (Overlay & Menus - `#21262d`):** Command palette (`Cmd+K`), dropdown menus, autocomplete popups, tooltip overlays. Contained by a crisp `1px solid #484f58` border and an ultra-subtle directional lift (`0 8px 24px rgba(0, 0, 0, 0.65)`).

## Shapes

The design system enforces an intentional, near-orthogonal geometric footprint (`roundedness: 1`). Compact radiuses reinforce the sense of a precision instrument:

- **Workspaces, Tabs, Toolbars, Panes:** `0px` radius (strictly flush, hard structural joins).
- **Buttons, Inputs, Badges, Autocomplete Rows:** `4px` radius (`rounded-sm` / `0.25rem`).
- **Modal Dialogs, Command Palettes, Float Cards:** `6px` radius (`0.375rem`) bounded by crisp single-pixel rules.
- **Status Dots & Pill Counter Indicators:** Fully round (`9999px`) where circular geometry conveys discrete state or telemetry.

## Components

### Primary Action Button ("Run Code")
- **Default:** Background `#ef4444`, foreground `#ffffff`, font `JetBrains Mono` 12px / 600 weight. Height `28px`, horizontal padding `12px`, border-radius `4px`. Features an inline trailing/leading SVG glyph (`Play` triangle).
- **Hover:** Background `#dc2626`.
- **Active / Pressed:** Background `#b91c1c`, transform `scale(0.99)`.
- **Focus:** `2px` solid `#f87171` outline offset by `2px`.

### Secondary & Utility Chrome Buttons
- **Default:** Background `transparent`, border `1px solid #30363d`, text `#f0f6fc`, height `28px`, padding `8px 10px`.
- **Hover:** Background `#21262d`, border color `#8b949e`.

### Tabs (Editor & Terminal)
- **Active Tab:** Surface `#0d1117`, text `#f0f6fc`, border-top `2px solid #ef4444`, border-right `1px solid #30363d`, border-left `1px solid #30363d`. Monospaced or Geist 12px text with a `6px` close cross (`x`) that shifts from `#484f58` to `#f0f6fc` on hover.
- **Inactive Tab:** Surface `#161b22`, text `#8b949e`, border-right `1px solid #21262d`, border-top `2px solid transparent`.
- **Hover Tab:** Text `#f0f6fc`, background `#1a202c`.

### Line Numbers & Code Gutter
- Fixed-width column right-aligned, text `#484f58`, font `JetBrains Mono` 13px.
- **Active Line Number:** Foreground `#f0f6fc`, bolded.
- **Active Line Highlighting:** Background layer across the code buffer at `#161b2280` (`rgba(22, 27, 34, 0.5)`).

### Status Badges & Terminal Chips
- Height `18px`, padding `0 6px`, font `JetBrains Mono` 10px uppercase with `0.04em` tracking.
- **Success/Live:** Surface `rgba(16, 185, 129, 0.12)`, text `#10b981`, border `1px solid rgba(16, 185, 129, 0.3)`.
- **Warning:** Surface `rgba(245, 158, 11, 0.12)`, text `#f59e0b`, border `1px solid rgba(245, 158, 11, 0.3)`.
- **Info/Branch:** Surface `rgba(56, 189, 248, 0.12)`, text `#38bdf8`, border `1px solid rgba(56, 189, 248, 0.3)`.

### Inputs & Command Filter
- Background `#090d13`, border `1px solid #30363d`, text `#f0f6fc`, placeholder `#484f58`.
- Focus state switches border to `#38bdf8` without external box-shadow bloom.

### File Tree & Hierarchy Lists
- Item row `24px` height, font `Geist` 13px. Hover row background `#21262d`. Active selected row background `rgba(56, 189, 248, 0.08)`, text `#f0f6fc`, accented with an optional `2px` sky-blue left border edge.