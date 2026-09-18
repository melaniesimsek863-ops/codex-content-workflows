# Human Voice Pass

This pass adapts ideas from Humanizer-zh (`https://github.com/op7418/Humanizer-zh`) for AI comic drama writing. Use it to improve voice quality, not to bypass detectors. The goal is better writing: concrete, character-specific, emotionally credible, and less formulaic.

## When To Use

Use on:

- dialogue
- narration
- opening hooks
- episode intros and recaps
- character inner monologue
- short-video captions/subtitles
- title options, cover text, and posting copy
- emotional prose after the story structure is already working

Do not use on:

- image prompts
- storyboard table columns
- worldbuilding ledgers
- timeline, hook, mystery, or power ledgers
- structured character fields
- technical production notes where consistency matters more than style

## Core Principles

1. Preserve meaning, plot facts, character intent, and continuity.
2. Remove AI-shaped filler: empty praise, generic summary, over-explaining, and polished-but-dead prose.
3. Make the voice belong to a person in a situation, not a neutral assistant.
4. Prefer concrete detail over abstract emotion.
5. Vary rhythm. Mix short hits with longer pressure-building sentences.
6. Keep useful messiness: hesitation, silence, unfinished thought, contradiction, and subtext.
7. Do not make every character sound like the same casual narrator.

## AI Trace Checklist For Chinese Scripts

Scan for these patterns:

- inflated meaning: `这不仅是...更是...`, `标志着`, `展现了`, `具有重要意义`
- generic AI connectors: `此外`, `然而`, `值得注意的是`, `总而言之`, `与此同时` when they add no dramatic turn
- empty intensity: `极其`, `深刻`, `复杂`, `关键`, `重要`, `强烈` without a concrete action
- fake balance: `一方面...另一方面...` when no real tension exists
- three-item rhythm repeated too often
- quote-card lines that sound written for screenshots rather than spoken by the character
- emotion labels without behavior: `她很崩溃`, `他十分愤怒`, `空气中弥漫着尴尬`
- over-clean exposition where characters explain what both already know
- assistant residue: `当然`, `希望这有帮助`, `下面是`, `我们可以看到`
- generic positive closure: `未来充满希望`, `一切都会越来越好`

## Rewrite Moves

### Replace Abstract Emotion With Action

Weak:

`她很难过，意识到自己一直被欺骗。`

Better:

`她盯着那条转账记录看了很久，手指停在屏幕上，没再往下滑。`

### Put Exposition Into Pressure

Weak:

`他解释说这栋楼二十年前发生过事故，所以大家都害怕十三层。`

Better:

`保安按住电梯门，声音压得很低：“十三层不送外卖。二十年前送过一次，没下来。”`

### Give Each Character A Speaking Habit

Before polishing, identify the speaker type:

- hides pain with jokes
- speaks like issuing orders
- avoids direct confession
- asks questions to control others
- uses official language when afraid
- says too little when guilty
- over-explains when lying

Polish lines according to the character, not a universal natural style.

### Break Formulaic Rhythm

If three consecutive sentences have the same shape, change one into an action, one into silence, or one into a fragment.

### Remove Gold-Quote Smell

If a line sounds like it wants to be highlighted, test whether the character would say it under pressure. If not, rewrite it as action, interruption, or a simpler line.

## Pass Procedure

1. Mark text type: dialogue, narration, hook, subtitle, title, or posting copy.
2. Identify the speaker or narrative voice.
3. Scan for AI trace checklist items.
4. Rewrite only the affected sentence/line first.
5. Check continuity: facts, clues, relationship state, and episode hook must remain unchanged.
6. Check voice separation: two characters should not become the same person.
7. Return a short `Human Voice Notes` section listing what changed.

## Output Format

When polishing a draft, provide:

```text
Human Voice Notes:
- Removed: [AI trace or stiff pattern]
- Strengthened: [concrete detail / subtext / rhythm / character voice]
- Preserved: [plot fact / clue / relationship beat]

Polished Version:
[revised text]
```

For full scripts, do not rewrite everything if only a few lines have problems. Preserve the script structure and polish the weak lines in place.