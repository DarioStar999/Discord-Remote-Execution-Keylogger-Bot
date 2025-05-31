<h1>Discord Remote Execution & Keylogger Bot <small>(Educational)</small></h1>

<p>This Python script demonstrates a Discord bot with remote code execution and keylogging features. <strong>It is intended for educational purposes only.</strong></p>

<h2>Main Features</h2>
<ul>
  <li><strong>Persistence:</strong> Automatically copies itself to the Windows Startup folder to run at system boot. (autorun version)</li>
  <li><strong>Debugger Detection:</strong> Monitors if a debugger is attached and tries to interfere by allocating large memory blocks.</li>
  <li><strong>Keylogger:</strong> Captures keystrokes and saves them to a <code>test.txt</code> file.</li>
  <li><strong>Discord Bot Commands:</strong>
    <ul>
      <li><code>!exc-&lt;code&gt;</code> - Execute arbitrary Python code remotely.</li>
      <li><code>!exc-ramfucker-&lt;size&gt;</code> - Send large strings to test memory usage.</li>
      <li><code>!getkey</code> - Retrieve the logged keystrokes.</li>
      <li><code>!help</code> - Show available commands.</li>
    </ul>
  </li>
</ul>

<div class="warning">
⚠️ <strong>Warning:</strong> This script is for educational use only. Misuse, especially without authorization, can be illegal and violate privacy.
</div>

</body>
</html>
