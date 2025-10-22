<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>TurnBound: Heroes vs. Creatures</title>
</head>
<body style="font-family: Arial, sans-serif; line-height: 1.6; color: #222; background-color: #fafafa; padding: 20px;">

  <h1>⚔️ <strong>TurnBound: Heroes vs. Creatures</strong></h1>

  <p>
    <strong>TurnBound</strong> was developed as a turn-based combat game where each character takes actions alternately 
    until one side is defeated. The project was created to apply Object-Oriented Programming concepts, focusing on 
    inheritance, class structure, methods, and clean code reuse.
  </p>

  <h2>🧱 Main Classes</h2>
  <ul>
    <li>🧬 <strong><code>Character</code> (base class)</strong> — responsible for common attributes such as 
      <code>name</code>, <code>health</code>, and <code>level</code>.</li>
    <li>🦸 <strong><code>Hero</code> (child class)</strong> — inherited from <code>Character</code> and received an 
      additional attribute called <code>ability</code>.</li>
    <li>👾 <strong><code>Enemy</code> (child class)</strong> — also inherited from <code>Character</code> and included 
      its own attribute called <code>type</code>.</li>
  </ul>

  <h2>📜 Character Details</h2>
  <p>
    A method was also created to display character details, showing:
  </p>
  <ul>
    <li>name, health, and level</li>
    <li><strong>+ the ability (for heroes)</strong> or <strong>the type (for enemies)</strong></li>
  </ul>

  <h2>🚀 Conclusion</h2>
  <p>
    With this structure, the foundation of a turn-based battle system was established, allowing future expansions 
    such as attack actions, defense, character evolution, and new types of heroes or enemies. The project successfully 
    reinforced Object-Oriented Programming principles by prioritizing clarity, organization, and code reusability.
  </p>

</body>
</html>
