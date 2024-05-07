/** @type {import('tailwindcss').Config} */
export default {
    content: [
        "./index.html",
        "./src/**/*.{vue,js,ts,jsx,tsx}",
        "./app/templates/index.html",
        "./app/static/src/**/*.{vue,js,ts,jsx,tsx}",
    ],
    theme: {
        extend: {
            listStyleType: {
                disc: 'disc',
                decimal: 'decimal',
            },
        },
    },
    plugins: [],
}

