import logo from './logo.png';
import './App.css';
import { Diagram } from './Diagram';

function App() {
  return (
    <div className="App">
      <div>
        <img src={logo} className="logo-pic" alt="logo" />
      </div>
      <div>
        <Diagram/>
      </div>
    </div>
  );
}

export default App;
