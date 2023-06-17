export default defineAppConfig({
  alpine: {
    title: "ani-voice",
    description: "A voice changer and translator software for all",
    footer: {
      navigation: true, // possible value are : true | false
      alignment: "center", // possible value are : 'none' | 'left' | 'center' | 'right'
      message: "Follow me on", // string that will be displayed in the footer (leave empty or delete to disable)
    },
    socials: {
      twitter: "lekiet0101",
      instagram: "lekiet0101",
      linkedin: {
        icon: "uil:linkedin",
        label: "LinkedIn",
        href: "https://www.linkedin.com/in/lekiet0101/",
      },
    },
    form: {
      successMessage: "Message sent. Thank you!",
    },
  },
});
