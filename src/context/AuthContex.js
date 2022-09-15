import ContextoAuth from "./Contexto";
import { useEffect, useState } from "react";
import { GoogleAuthProvider, signInWithPopup, createUserWithEmailAndPassword, signInWithEmailAndPassword, onAuthStateChanged, signOut, sendPasswordResetEmail } from "firebase/auth";
import { auth } from "../services/firebase";

export default function AuthContex(props) {
    const { children } = props;
    //registro
    const signup = (email, password) => {
        return createUserWithEmailAndPassword(auth, email, password);
    };
    //logeo usuario y contraseña
    const login = (email, password) => {
        return signInWithEmailAndPassword(auth, email, password);
    };
    // logeo por gmail
    const loginWithGoogle = () => {
        const googleProvider = new GoogleAuthProvider();
        return signInWithPopup(auth, googleProvider);
    };
    // cerrar session
    const logout = () => signOut(auth);
    //Se comprueba si el usuario esta logeado o no
    const [user, setUser] = useState(null);
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        const unsubuscribe = onAuthStateChanged(auth, (currentUser) => {
            setUser(currentUser);
            setLoading(false);
        });
        return () => unsubuscribe();
    }, []);
    return (
        <>
            <ContextoAuth.Provider value={{
                signup,
                login,
                user,
                loading,
                loginWithGoogle,
                logout
            }}>
                {children}
            </ContextoAuth.Provider>
        </>
    )
}
