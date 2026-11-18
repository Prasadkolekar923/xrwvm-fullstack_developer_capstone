import React, { useState } from 'react';
import './Register.css';
import userIcon from '../assets/person.png';
import emailIcon from '../assets/email.png';
import passwordIcon from '../assets/password.png';
import closeIcon from '../assets/close.png';
export default function Register() {
  const [form, setForm] = useState({ userName: '', firstName: '', lastName: '', email: '', password: '' });
  const [error, setError] = useState('');
  const update = (key) => (event) => setForm({ ...form, [key]: event.target.value });
  const submit = async (event) => {
    event.preventDefault(); setError('');
    try {
      const response = await fetch(window.location.origin + '/djangoapp/register', { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify(form) });
      const data = await response.json();
      if (!response.ok) throw new Error(data.error || 'Registration failed');
      sessionStorage.setItem('username', data.userName); window.location.assign('/');
    } catch (err) { setError(err.message); }
  };
  return <main className="register_container" style={{ width: '50%' }}>
    <header className="header"><span className="text">Sign Up</span><a href="/" aria-label="Close"><img style={{ width: '1cm' }} src={closeIcon} alt="Close" /></a><hr /></header>
    {error && <p role="alert">{error}</p>}
    <form onSubmit={submit}><div className="inputs">
      <label className="input"><img className="img_icon" src={userIcon} alt=""/><input required placeholder="Username" value={form.userName} onChange={update('userName')} /></label>
      <label className="input"><img className="img_icon" src={userIcon} alt=""/><input placeholder="First Name" value={form.firstName} onChange={update('firstName')} /></label>
      <label className="input"><img className="img_icon" src={userIcon} alt=""/><input placeholder="Last Name" value={form.lastName} onChange={update('lastName')} /></label>
      <label className="input"><img className="img_icon" src={emailIcon} alt=""/><input required type="email" placeholder="Email" value={form.email} onChange={update('email')} /></label>
      <label className="input"><img className="img_icon" src={passwordIcon} alt=""/><input required type="password" placeholder="Password" value={form.password} onChange={update('password')} /></label>
    </div><div className="submit_panel"><button className="submit" type="submit">Register</button></div></form>
  </main>;
}
