import Link from 'next/link';

export const Header = () => {
    return (
        <header className="header">
            <div className="logo">Echo</div>
            <nav className="nav">
                <Link href="/">Dashboard</Link>
                <Link href="/technology">Technology</Link>
                <Link href="/tutorial">Tutorial</Link>
                <Link href="/documentation">Documentation</Link>
                <Link href="/the-creator">The Creator</Link>
            </nav>
        </header>
    );
};