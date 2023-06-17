export default defineAppConfig({
  alpine: {
    title: 'ani-voice',
    description: 'A voice changer and translator software for all',    
    header: {
      position: 'right', // possible value are : | 'left' | 'center' | 'right'
      logo: {
        path: '/favicon.ico', // path of the logo
        pathDark: '', // path of the logo in dark mode, leave this empty if you want to use the same logo
        alt: 'ani-voice' // alt of the logo
      }
    },
    footer: {
      credits: {
        enabled: false, // possible value are : true | false
        repository: 'https://www.github.com/nuxt-themes/alpine' // our github repository
      },
      navigation: true, // possible value are : true | false
      alignment: 'center', // possible value are : 'none' | 'left' | 'center' | 'right'
      message: 'Follow me on' // string that will be displayed in the footer (leave empty or delete to disable)
    },
    socials: {
      twitter: 'lekiet0101',
      instagram: 'lekiet0101',
      linkedin: {
        icon: 'uil:linkedin',
        label: 'LinkedIn',
        href: 'https://www.linkedin.com/in/lekiet0101/'
      }
    },
    form: {
      successMessage: 'Message sent. Thank you!'
    }
  }
})
