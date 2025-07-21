import React from 'react';
import { createRoot } from 'react-dom/client';
import CrepeEditor from './CrepeEditor';
import './style.css';

const element = document.getElementById("root")
const root = createRoot(element as HTMLElement)

root.render(
  <CrepeEditor />
)
